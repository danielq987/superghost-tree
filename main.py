#!/usr/bin/python

import json
import time
from string import ascii_lowercase
from query import possible_words, load_words

def main():
  startTime = time.time()
  # load words into word_list, ~ 60000 words
  twoLetters = load_words("logs/twoLetters.txt")
  word_list = load_words("words/ubuntu_f.txt")
  # for i in ascii_lowercase:
  #   for j in ascii_lowercase:
  #     twoLetters[i + j] = possible_words(i + j, word_list)

  
  # return all 2letter substrings with <10 words continuations
  for item in twoLetters.items():
    if item[1] < 10:
      possible = possible_words(item[0], word_list)
      for i in possible:
        if len(i) % 2 == 1:
          print(f"{item[0]}: {possible}")
          break

  # with open('logs/twoLetters.txt', 'w') as fout:
  #   fout.write(json.dumps(twoLetters))

  endTime = time.time()
  print(f"Program completed in {round(endTime - startTime, 2)} seconds")


if __name__ == "__main__":
  main()