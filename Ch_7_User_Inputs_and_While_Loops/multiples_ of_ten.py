# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:57:47 2018

@author: ACANTAMA
"""

multiple_10 = input("Tell me a number and I'll tell you if it's a multiple of 10. ")
multiple_10 = int(multiple_10)

if multiple_10 % 10 == 0:
    print("\nThe number " + str(multiple_10) + " is a multiple of 10.")
else:
    print("\nThe number " + str(multiple_10) + " is not a multiple of 10.")