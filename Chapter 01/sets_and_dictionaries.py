#!/bin/env python

# To use the newer style of print
from __future__ import print_function

# The list has values within the range 1 to 100
print(list(range(1,100)))

# Sets in Python
# A set is an unordered collection with no duplicate elements
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# To print the complete set
print("set: ", basket)

# To test for membership in the set
print("'orange' in basket : ", 'orange' in basket)
print("'crabgrass' in basket : ", 'crabgrass' in basket)

# Dictionaries in Python
# Create a dictionary
dic = {'IBM' : 658.42, 'INTEL' : 432.80}

# To print the dictionary
print("dic : ", dic)

# To append another key/value pair
dic['CISCO'] = 217.55

# To print the dictionary
print("dic : ", dic)

# To print the specific value for a key
print("dic['IBM]' : ", dic['IBM'])

# To delete a key/value pair from the dictionary
del dic['INTEL']

# To print the dictionary
print("dic : ", dic)

# To find the key in the dictionary
print("'IBM' in dic : ", 'IBM' in dic)

# To check if something is not in the dictionary
print("'CISCO' not in dic : ", 'CISCO' not in dic)
