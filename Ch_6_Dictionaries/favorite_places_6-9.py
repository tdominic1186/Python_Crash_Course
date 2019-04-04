# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:57:11 2018

@author: ACANTAMA
"""

favorite_places = {
        'tony': ['new zealand', 'valley forge'],
        'jess': ['italy', 'montreal'],
        'michelle': ['australia', 'germany'],
        'kyle': ['germany'],
        }

for name, places in favorite_places.items():
    if len(places) > 1:
        print(name.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place.title())
    else:
        print(name.title() + "'s favorite place is:")
        for place in places:
            print("\t" + place.title())