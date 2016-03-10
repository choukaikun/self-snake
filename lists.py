#!/bin/env python

# To use the newer style of print
from __future__ import print_function

# Lists in Python
my_list = ['Python Programming', 100, 92.75, 'john', 82.3]
tinylist = [80, 82, 73, 64, 85]

# To print the complete list
print("my_list: ", my_list)
print("tinylist: ", tinylist)

# To print the first element of the list
print("my_list[0]: ", my_list[0])
# To print elements 2 through 3
print("my_list[1:3]", my_list[1:3])

# To print all elements starting from the 3rd element
print("print elements starting from the 3rd element: ")
print(my_list[2:])

# To print the list two times
print("list two times: ", tinylist * 2)

# To print the lists concatenated
print("concatenated lists: ", my_list + tinylist)

