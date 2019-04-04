#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:34:52 2018

@author: Tony_MBP
"""
"""
creates a list from one to one million, prints min, max, and sum. commented out
processs to test one to two at a time.
"""
numbers = []
for value in range(1,100000001):
    numbers.append(value)
#print(min(numbers))
#print(max(numbers))
print(sum(numbers))