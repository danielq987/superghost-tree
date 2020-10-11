import json
import time

def load_words(filepath):
  """
  loads words from filepath
  """
  with open(filepath) as f:
    return json.load(f)

def possible_words(substr, word_list):
  """
  given a substring, returns a list of all possible words with that substring
  """
  temp = []
  for i in word_list:
    if substr in i:
      temp.append(i)
  return temp
  # count = 0
  # for i in word_list:
  #   if substr in i:
  #     count += 1

  # return count

def main():
  startTime = time.time()

  word_list = []
  with open("words/american-english.txt") as f:
    for i in f:
      word_list.append(i.strip())

  print(len(word_list))

  word_list = [i for i in word_list if i.isalpha() and i.islower()]  
  word_list = [i for i in word_list if len(i) >= 4]

  endTime = time.time()
  print(f"listcomp 1 in {round(endTime - startTime, 2)} seconds")
  
  endTime = time.time()
  print(f"listcomp 2 in {round(endTime - startTime, 2)} seconds")

  print(len(word_list))

  with open("words/dict.txt", 'w') as fout:
    fout.write(json.dumps(word_list))

  endTime = time.time()
  print(f"Program completed in {round(endTime - startTime, 2)} seconds")

if __name__ == "__main__":
  main()