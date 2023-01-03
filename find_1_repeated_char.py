comm='''
Tech Challenge in Python: Find the first repeated character in a string

Pseudocode 1:
1) find the character that occurs more than once
2) example:
    2.1) input = 'geek app'; output = e
    2.2) input = 'hello cool guys'; output = l
3) run 2 nested loops
4) traverse from left to right to check if a letter / character repeats or not
5) if letter / character repeats, increment count of repeating characters
6) when the count becomes K, return the character

Pseudocode 2:
1) Create an empty hash.
2) Scan each character of input string and insert values to each keys in the hash.
3) When any character appears more than once, hash key value is increment by 1, and return the character.
'''
