# superghost-solver

This is my attempt at solving Superghost using Python, by using a game tree.

Information about the game can be found here. https://www.wikiwand.com/en/Ghost_(game)

## About the Program

**Disclaimer:** Please don't use this program to generate a tree yourself, unless your word list is rather small (<10000 words). The code here is the code I used, but making a graph of ~60000 words took around 6 hours, which definitely does not seem like the most efficient way.

This repository is solely for making the tree itself, with the main code in tree.py. The game tree is roughly stored in a dictionary structure, where the keys represent the possible substrings which can be achieved over the process of the game. The values of each key is a list of the children of the substring. For example, the key "psychoanalyzin" has exactly one child in my tree, "psychoanalyzing", since it is the only possible word that can be spelt with the substring "psychoanalyzing".

The file tree/tree.p is the final tree. To use it, use the pickle module in python to load it.
```
pickle.load(open("tree/tree.p", "rb"))
```
In addition, make sure the file treeClasses.py is in the same directory, since the graph is a custom python object, and will probably not work properly without the class declarations.

## Additional Information

Creating this tree spawned two other projects:
- A bot which can play Superghost flawlessly
- An explorer which can explore tree/tree.p, finding optimal moves and examining each of the ~380000 nodes in the tree.

You can find these two projects on my GitHub page, linked below.

https://github.com/danielq987/superghost-computer

https://github.com/danielq987/superghost-explorer

As well, more detailed information about this project can be found on my non-existant blog (hopefully up soon!).
