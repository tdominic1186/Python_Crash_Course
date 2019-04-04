#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:32:45 2018

create a dictionary of someone you know and print each value

@author: Tony_MBP
"""

person_0 = {
        'first_name': 'tony',
        'last_name': 'cantamaglia',
        'age': 31,
        'city': 'philadelphia',
        }

person_1 = {
        'first_name': 'jess',
        'last_name': 'colliver',
        'age': 28,
        'city': 'philadelphia',
        }
person_2 = {
        'first_name': 'dave',
        'last_name': 'oxenford',
        'age': 30,
        'city': 'thurmont',
        }

people = [person_0, person_1, person_2]

for person in people:
    print("\nFirst name: " + person ['first_name'].title())
    print("Last name: " + person ['last_name'].title())
    print("Age: " + str(person ['age']))
    print("City of Residence: " + person ['city'].title())