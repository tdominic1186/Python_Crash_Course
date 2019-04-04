#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:02:39 2018

make a list of multiples of 3 from 3 to 30. use a for loop to print the numbers
in your list.

@author: Tony_MBP
"""

numbers = []
for value in range(3,31,3):
    numbers.append(value)
print(numbers)