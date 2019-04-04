# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:39:34 2018

@author: ACANTAMA
"""

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input(name.title() + ", if you could visit one place in the world, \
where would you go? ")
    
    responses[name] = vacation
    
    repeat = input("Now that you've submitted your response to the poll, \
would you like to let someone else respond? (yes/ no) ")
    
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(name.title() + " would like to vist " + vacation.title() + ".")