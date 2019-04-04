# -*- coding: utf-8 -*-
"""
Created on Sat May 12 20:16:17 2018

@author: ACANTAMA
"""

sandwich_orders = ['roast beef', 'tuna', 'reuben', 'banh mi']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\nAll sandwiches have been made.")