# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:06:23 2018

@author: ACANTAMA
"""

favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edwara': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())