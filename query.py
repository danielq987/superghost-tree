import json
import time

"""
Miscellaneous functions unrelated to making the tree
"""

def loadWords(filepath):
  """
  loads words from filepath
  """
  with open(filepath) as f:
    return json.load(f)

def possibleWords(substr, word_list):
  """
  given a substring, returns a list of all possible words with that substring
  # """
  temp = []
  for i in word_list:
    if substr in i:
      temp.append(i)
  return temp

def isWord(word, word_list):
  if word in word_list:
    return True
  else:
    return False

def filter(word_list):
  """
  filters the wordlist, a list
  """
  print(f"Length before filtering: {len(word_list)}")
  
  word_list = [i for i in word_list if i.isalpha() and i.islower()]  
  word_list = [i for i in word_list if len(i) >= 4]

  print(f"Length after filtering: {len(word_list)}")
  
  return word_list

def main():
  """
  filters the wordlist
  """
  # filters the word list to remove 
  startTime = time.time()

  # opens dictionary
  with open("words/u.txt") as f:
    word_list = json.load(f)
  
  word_list = filter(word_list)

  with open("words/ubuntu_f.txt", 'w') as fout:
    fout.write(json.dumps(word_list))

  endTime = time.time()
  print(f"Program completed in {round(endTime - startTime, 2)} seconds")

if __name__ == "__main__":
  main()