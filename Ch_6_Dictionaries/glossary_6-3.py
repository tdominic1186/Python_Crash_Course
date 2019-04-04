#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:51:17 2018

create a glossary of programming terms and their meaninings. print the words and their meanings as formatted text

@author: Tony_MBP
"""

programming_glossary = {
        'list': 'a collection of values.',
        'variable': 'an object that contains a value.',
        'tuple': 'an immutable list.',
        'value': 'an object that is assigned to a variable, list, tuple, etc.',
        'dictionary': 'a collection of keys and corresponding values.',
        'method': 'a function that is used to modify an object.',
        'integer': 'a whole number.',
        'mutable': 'an object that can be changed.',
        'immutable': 'an object that cannot be changed.',
        'whitespace': 'spacing before or after a string of characters.',
        }

for key, value in programming_glossary.items():
    print(key.title() + " - " + value.capitalize() + "\n")