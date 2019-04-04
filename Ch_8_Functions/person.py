# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:23:47 2018

p144

@author: ACANTAMA
"""

def build_person(first_name, last_name, age=''):
    """Return a dictionary of informatuon about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)