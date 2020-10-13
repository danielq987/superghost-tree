from treeClasses import Graph, Node, Edge # tree elements
from query import loadWords, isWord # query functions
from string import ascii_lowercase
from tree import loadTree # load tree from .p file
import json
import time
import pickle

def main():
  tree = loadTree("tree/treeWinner.p")
  print("Explore the SuperGhost Tree!")
  with open("help.txt", "r") as f:
    helptext = f.read()
  while True:
    line = input(">> ")
    if line == "":
      continue
    elif line == "exit":
      print("cya bich")
      break
    elif line == "help" or line == "h":
      print(helptext)
    elif line[0] == "-":
      word = line[1:].strip()
      turn = len(word) % 2 + 1
      print(f"Player {turn}'s turn.")
      a = tree.getNode(word)
      if type(a) == int:
        print("Bad string - no moves possible.")
        continue
      children = tree.getChildren(a)
      if len(children) == 0:
        print(f"{word} is a word! Player {a.getWinner()} wins.")
        continue
      winning = []
      for i in children:
        if i.getWinner() == turn:
          winning.append(i.getName())
      if len(winning) == 0:
        print(f"No winning moves for Player {turn}.")
      else:
        print(f"Winning moves for Player {turn}:")
        for i in winning:
          print(i)
    else:
      print("Invalid command. Type help for help.")
          


if __name__ == "__main__":
  main()