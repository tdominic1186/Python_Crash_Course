#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:21:36 2018

@author: Tony_MBP
"""


guests = ['Christian Bale', 'Heath Ledger', 'Neil DeGrasse Tyson']

print(guests[0] + ", as Batman you are cordially invited to dinner.")
print(guests[1] + ", as the Joker, you can come to dinner but please behave.")
print(guests[2] + ", can you please come to dinner at my place?")

print(guests[1] + " can't make it.")
del guests[1]
guests.insert(1, "Christopher Nolan")

print(guests[0] + ", as Batman you are cordially invited to dinner.")
print(guests[1] + ", as Batman's director you can come to dinner instead of\
 Heath.")
print(guests[2] + ", can you please come to dinner at my place?")