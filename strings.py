#!/bin/env python

# To use the newer style of print
from __future__ import print_function

# Strings in Python
text = 'Hello World!'

# If you see an output message complete string
print(text)

# You will get the first character of the string
print("First character of the string: ", text[0])

# You will get the characters from the 3rd to the 5th
print("The string from the 3rd character to the 5th: ", text[2:5])

# You will get the characters from the 3rd to the end of the string
print("The string the 3rd character to the end: ", text[2:])

# To print the string two times
print("The string two times: ", text * 2)

# To print the string concatenated with "TEST"
print("The string concatenated: ", text + "TEST")
