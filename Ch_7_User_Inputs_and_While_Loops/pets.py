# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:18:09 2018

@author: ACANTAMA
"""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)