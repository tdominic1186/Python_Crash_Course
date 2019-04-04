#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:48:38 2018

lists pizzas and copies as friend_pizzas

@author: Tony_MBP
"""

pizzas = ['pepperoni', 'sausage', 'mushroom']
friend_pizzas = pizzas[:]

pizzas.append('onion')
friend_pizzas.append('margherita')

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza.title())
    
print("\nMy friend's favorite pizzas are:")
for pizza_f in friend_pizzas:
    print(pizza_f.title())
print("\n-------")
    


"""
"""