# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:21:35 2018

@author: ACANTAMA
"""

sandwich_orders = ['roast beef', 'pastrami', 'tuna', 'pastrami', 'reuben', 'pastrami', 'banh mi']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("The deli has run out of pastrami.")
    print("\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')        

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\nAll sandwiches have been made.")
