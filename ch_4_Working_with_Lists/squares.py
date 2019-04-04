#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:34:07 2018

@author: Tony_MBP
"""

"""
square and appends the result to list of squares
"""

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)
print("\n-----")

"""
same as above but cleaner
"""
squares = []
for value in range(1,11):
    squares.append(value**2)
    
print(squares)
print("\n-----")

"""
same as above but using list comprehension
"""
squares = [value**2 for value in range(1,11)]
print(squares)
print("\n-----")