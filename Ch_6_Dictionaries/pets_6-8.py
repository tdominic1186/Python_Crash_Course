# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:49:33 2018

@author: ACANTAMA
"""

cooper = {
        'species': 'dog',
        'color': 'brown',
        'owner': 'tony',
        }

nemo = {
        'species': 'fish',
        'color': 'orange',
        'owner': 'terry',
        }

dexter = {
        'species': 'cat',
        'color': 'gray',
        'owner': 'raff',
        }

pets = [cooper, nemo, dexter]

for pet in pets:
    print("\nThis pet's species is " + pet ['species'] + ".")
    print("This pet's color is " + pet ['color'] + ".")
    print("This pet's owner is " + pet ['owner'].title() + ".")

