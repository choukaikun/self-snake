#!/bin/env python

# To use the newer style of print
from __future__ import print_function

# Conditional statements in Python
var = 100

if var:
    print("A true expression value")
    print(var)

# if and else statement
# the value var is null or zero
# the condition is not satisfied and moved to the else statement

var = 0

if var:
    print("A true expression value")
    print(var)
else:
    print("Good bye!")

# while statement

count = 0
while count < 5:
    print('The count is:', count)
    count += 1
print("Good bye!")

# arithmetic progressions using range method with for loop

for var in range(5):
    print(var)
