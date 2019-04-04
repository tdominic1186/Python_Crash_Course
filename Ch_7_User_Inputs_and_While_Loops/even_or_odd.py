# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:40:53 2018

@author: ACANTAMA
"""

number = input("Enter a number and I'll tell if it's even or odd. ")
number = int(number)

if number % 2 == 0:
    print("\nThe numeber " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")