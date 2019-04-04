# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:27:22 2018

p146

@author: ACANTAMA
"""

def city_country(city, country):
    """Returns a neatly formatted string of 'city, country'"""
    output = city + ", " + country
    return output.title()

location = city_country('auckland', 'new zealand')
print(location)

location = city_country('paris', 'france')
print(location)

location = city_country('beijing', 'china')
print(location)

