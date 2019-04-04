#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:53:53 2018

@author: Tony_MBP
"""

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

"""
#print("Sarah's favorite language is " + favorite_languages ['sarah'].title() + '.')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
"""
"""
#print name of each person that took the poll in alphabetical order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll." )
"""    

"""
#print favorite language of each person in dictionary and if in friends list print a special message. also is 'erin' not in dictionary, print a special message
friends = ['phil', 'edward']

for name in sorted(favorite_languages.keys()):
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
"""

"""
#print only values
print("The following messagges have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
"""

#print distinct values
print("The following values have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())