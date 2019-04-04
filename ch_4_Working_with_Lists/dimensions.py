#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:17:01 2018

@author: Tony_MBP
"""

dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

#dimensions[0] = 250

#print(dimensions[0])
#print(dimensions[1])

print("\n-----")
    
"""
writing over a tuple
"""

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
