# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:21:20 2018

@author: ACANTAMA
"""

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'joe', 'steve', 'kyle']

for person in people_to_poll:
    if person not in favorite_languages:
        print("Hey, " + person.title() + ", why don't you take our poll?")
    else:   
        print("Thanks, " + person.title() + ", for taking our poll.")