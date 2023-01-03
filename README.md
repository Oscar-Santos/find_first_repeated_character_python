![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
### Python Tech Challenge : 'Find the first repeated character in a string'

#### Overview
I am learning Python, and I found this tech challenge, I did 2 parts for this challenge, first I wrote 2 examples of pseudocode, and then I wrote the actual Python code.
#### Pseudocode
```
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
```

#### Actual Code

```
def first_repeated_char(str):

    hash = {}

    for ch in str:
        if ch in hash:
            return ch;
        else:
            hash[ch] = 0
    return ''

print(first_repeated_char('geek app'))
# terminal output: e

print(first_repeated_char('hello cool guys'))
# terminal output: l

print(first_repeated_char('cool weather'))
# terminal output: o
```


