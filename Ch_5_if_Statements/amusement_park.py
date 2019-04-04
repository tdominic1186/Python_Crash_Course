#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:19:11 2018

if-elif-else chain

@author: Tony_MBP
"""

age = 12


if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
print("\n*************")

#same output but more efficient

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
print("\n***********")

#same output but extra elif for senior discount

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("Your admission cost is $" + str(price) +".")
print("\n***************")

#same output but else stmt is omitted

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your admission cost is $" + str(price) + ".")
        