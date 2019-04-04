#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:38:39 2018

create a dictionary of names and each persons's favorite number. print each name and the corresponding favorite number.

@author: Tony_MBP
"""

favorite_numbers = {
        'tony': 43,
        'jess': 10,
        'dave': 69,
        'kyle': 88,
        'drew': 13,
        }

for value, key in favorite_numbers.items():
    print(value.title() + " " + str(key))
