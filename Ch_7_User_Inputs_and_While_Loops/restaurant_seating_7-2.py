# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:51:41 2018

@author: ACANTAMA
"""

guests = input("How many are guests are in your party? ")
guests = int(guests)

if guests > 8:
    print("\nYou'll have to wait a bit for a table to open up for your party of " + str(guests) + ".")
else:
    print("\nWe have a table available for your party of " + str(guests) + ".")