# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:06:33 2018

@author: ACANTAMA
"""

rivers = {
        'nile': 'egypt',
        'yangtze': 'china',
        'volga': 'russia',
        }

#use a loop to print a sentence about each river
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print('\n')
    
#use a loop to print the name of each river
for river in rivers.keys():
    print(river.title())
print('\n')
    
#use a loop to print the name of each country
for country in rivers.values():
    print(country.title())
print('\n')