#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:25:38 2018

pretend you're at a restauraunt and think of five simple foods they offer
store the foods in a tuple and use a for loop to print each food the 
restauraunt offers

@author: Tony_MBP
"""
menu = ('chicken', 'beef', 'salmon', 'shrimp', 'caviar')

for food in menu:
    print(food.title())
    
print("\n-----")
    
"""
the restauraunt changes its menu and replaces two items with different foods.
rewrite the tuple  and use a for loop to to print each of the items on the
revised menu
"""

menu = ('chicken', 'beef', 'pizza', 'shrimp', 'sausage')
for food in menu:
    print(food.title())
