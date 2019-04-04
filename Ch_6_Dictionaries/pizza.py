# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 09:58:24 2018

@author: ACANTAMA
"""

#store information about a pizza being ordered
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }

#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)