from treeClasses import Graph, Node, Edge # tree elements
from query import loadWords, isWord
from string import ascii_lowercase
import json
import time
import pickle

"""
This file contains all the required functions to build a tree from a list of words, albeit slightly inefficiently
"""

# the wordlist to be used
word_list = loadWords("words/u.txt")

node_list = []

def makeNodes(word, graph):
  """
  for a given word/substring, make the required nodes in the graph
  """
  # should only be the case when all of the 1st level nodes have not been added yet
  if len(word) == 1:
    try:
      graph.addNode(Node(word, False))
      node_list.append(word)
      return 0
    except ValueError:
      return 0

  # recursively make nodes of word[:-1]
  try:
    # only creates the node if the left parent is not a word
    if not isWord(word[:-1], word_list):
      # only perform recusion if word[:-1] not a part of graph
      if word[:-1] not in node_list:
        makeNodes(word[:-1], graph)
      graph.addNode(Node(word, False))
      node_list.append(word)
  except ValueError:
    pass

  # recursively make nodes of word[1:]
  try:
    # only creates the node if the right parent is not a word
    if not isWord(word[1:], word_list):
      # only perform recusion if word[1:] not a part of graph
      if word[1:] not in node_list:
        makeNodes(word[1:], graph)
      graph.addNode(Node(word, False))
      node_list.append(word)
  except ValueError:
    pass

  return 0

def constructNodes():
  """calls makeNodes for each word in the word_list
  makes a tree from word_list, then returns it
  NOTE: takes ~2 minutes for a list of 9000 words"""
  tree = Graph()
  print(">> Started constructing nodes")
  count = 0
  leng = len(word_list)
  nodetime = time.time()
  for word in word_list:
    count += 1
    if count % 100 == 0:
      print(f"{count}/{leng} {word} in {round(time.time() - nodetime, 1)}")
    makeNodes(word, tree)
  
  print(">> Done constructing nodes!")

  return tree

def loadTree(filepath):
  """loads the already constructed tree from a .p file specified by filepath"""
  print(f">> Loading tree from {filepath}")
  return pickle.load(open(filepath, "rb"))

def dumpTree(tree, filepath):
  """dumps tree to filepath"""
  print(f">> Dumping to {filepath}")
  pickle.dump(tree, open(filepath, "wb"))

def addEdges(tree):
  """Assumes all nodes are in the tree. Adds the required edges.
  NOTE: this function is very slow -> for a graph with 60000 nodes, it takes up to 8 minutes."""

  print(">> Started adding edges")
  
  d = tree.edges     
  keys = d.keys()

  leng = len(keys)
  count = 0
  edgetime = time.time()

  # iterate over the keys and add edges for each node to 1 or 2 of its parents
  for node in keys:
    name = node.getName()
    # logging
    if count % 200 == 0:
      print(f"{count}/{leng} {name} in {round(time.time() - edgetime, 1)}")
    if len(name) != 1 and len(name) != 0:
      lparent = tree.getNode(name[:-1])
      if type(lparent) == Node:
        tree.addEdge(Edge(lparent, node))
      rparent = tree.getNode(name[1:])
      if type(rparent) == Node:
        tree.addEdge(Edge(rparent, node))
    elif name != "":
      tree.addEdge(Edge(tree.getRoot(), node))
    count += 1
  
  print(">> Done adding edges!")
  return tree

def wordFlag(tree):
  """
  If the node is a word, set its word attribute to True and delete all its children. 
  Relatively quick compared to adding nodes and edges.
  """
  print(">> Started adding word flags to valid words")

  d = tree.edges

  count = 0
  for i in d.keys():
    if count % 100 == 0:
      print(str(count) + " " + i.getName())
    if isWord(i.getName(), word_list):
      i.word = True
      tree.edges[i] = []
    count += 1

  print(">> Done adding word flags!")
  return tree

def makeTree():
  """
  Does everything at once. Might take awhile, especially for word_lists of over 10,000.
  """
  # adds all nodes to the tree
  tree = constructNodes()
  # adds all edges to the tree
  tree = addEdges(tree)
  # sets word attributes of nodes to True if they are valid words, and removes all their children
  tree = wordFlag(tree)
  # # assign a value of 1 or 2 to each word, representing which player wins when that word is spelt (for optimal play)
  # assignWinners(tree, "logs/test.txt")
  return tree

def inv(a):
  return 2 if a == 1 else 1

def traverse(visited, tree, node):
  """
  traverses through the tree recursively, and assigns a winner to each node
  """

  turn = (len(node.getName()) % 2) + 1
  children = tree.getChildren(node)
  if len(children) == 0:
      print(node.getName())
      node.setWinner(turn)
      visited[node.getName()] = turn
      return turn
  if node.getName() not in visited:
    winning = []
    for child in children:
      """child is a child of node"""
      if traverse(visited, tree, child) == turn:
        winning.append(child)
    if len(winning) > 0:
      node.setWinner(turn)
      visited[node.getName()] = turn
      return turn
    else:
      node.setWinner(inv(turn))
      visited[node.getName()] = inv(turn)
      return inv(turn)
  else:
    return visited[node.getName()]

def assignWinners(tree, filepath):
  """starts the recursive traverse() calls, and dumps the json with word:winner to filepath"""
  visited = {}

  print(">> Started traversing Tree")
  traverse(visited, tree, tree.getRoot())
  print(">> Done traversing Tree")

  print(len(visited))
  print(len(tree.edges))

  with open(filepath, "w") as f:
    f.write(json.dumps(visited))

def main():
  startTime = time.time()

  tree = loadTree("tree/tree.p")

  count = 0
  for edge in tree.edges.keys():
    if edge.getWinner()== 0:
      count += 1
      print(edge.getName())
  
  print(count)

  endTime = time.time()
  print(f"Program completed in {round(endTime - startTime, 2)} seconds")

if __name__ == "__main__":
  main()

