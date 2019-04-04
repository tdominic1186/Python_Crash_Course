#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:02:38 2018

More conditional tests.

@author: Tony_MBP
"""

print('test for equaility and inequality with strings')
print('tim' == 'time')
print('time' == 'time')

print('\ntests using the lower() function')
TIM = 'tim'
print(TIM.lower() == 'tim')
print(TIM.lower() == 'TIM')

print('\nNumerical tests involving equality and inequality, greater than and \
less than, greater than or equal to, and less than or equal to')

print(1 == 2)
print(1 == 1)
print(1 >= 2)
print(1 <= 2)
print(1 > 2)
print(1 < 2)

print('\ntests using the "and" keyword and the "or" keyword')

print(1 > 0 and 3 > 2)
print(1 > 0 or 3 > 1)
print(1 > 0 and 3 > 4)
print(1 > 2 or 3 > 4)

print("\nTest whether an item is and isn't in a list")

cars = ['audi', 'bmw', 'ford']
print('audi' in cars)
print('dodge' in cars)