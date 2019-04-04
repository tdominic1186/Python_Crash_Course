#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:28:48 2018

make a list of the first 10 cubes and use a for loop to print out the value of
each cube

@author: Tony_MBP
"""

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)
print("\n-----")


"""
using list comp and slices with a message stating "These are the first three:"
"""

cubes = [value**3 for value in range(1,11)]
print("The first three items in the list are: " + str(cubes[:3]) + ".")
print("\n-----")

"""
same as above, but slice middle and print a msg stating "These are middles:"
"""

cubes = [value**3 for value in range(1,11)]
print("Three items from the middle of the list are: " + str(cubes[4:7]))
print("\n-----")

"""
same as above, but slice last 3 and print stmt saying "These are last three:"
"""

cubes = [value**3 for value in range(1,11)]
print("The last three items in the list are: " + str(cubes[-3:]))