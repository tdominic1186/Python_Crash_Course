# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:00:10 2018

@author: ACANTAMA
"""

def describe_city(city, country='new zealand'):
    """Prints a city and the country it is in."""
    print(city.title() + " is in " + country.title() + ".")
    
describe_city('auckland')
describe_city('wellington')
describe_city(city='philadelphia', country='the united states')