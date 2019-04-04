# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:41:00 2018

@author: ACANTAMA
"""

favorite_numbers = {
        'tony': [43, 69, 143],
        'jess': [10, 126],
        'dave': [69, 99],
        'kyle': [88, 45],
        'drew': [13, 69, 11],
        }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))