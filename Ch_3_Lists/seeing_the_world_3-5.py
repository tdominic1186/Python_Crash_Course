#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:56:36 2018

@author: Tony_MBP
"""

places = ['new zealand', 'canada', 'uk', 'australia', 'japan']
print(places)
#use sorted to to print list alphabetically w/o modifying list
print(sorted(places))
#show list is still in same original order
print(places)
#use sorted to print list in reverse alpha w/o modifying list
print(sorted(places, reverse = True))
#show list is still in same order
print(places)
#use reverse to to change order of list and print
places.reverse()
print(places)
#use reverse to change order back
places.reverse()
print(places)
#use sort to change list to alpha and print to show changed order
places.sort()
print(places)
#use sort to change list to reverse alpha and print to show changed order
places.sort(reverse = True)
print(places)