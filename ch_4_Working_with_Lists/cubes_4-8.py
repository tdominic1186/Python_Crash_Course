#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:08:38 2018

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
using list comprehension
"""
cubes = [value**3 for value in range(1,11)]
print(cubes)
print("\n-----")
