#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:32:17 2018

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

print("Everyone, I found a bigger table!")

guests.insert(0, "Lolo Jones")
guests.insert(2, "Brian Dawkins")
guests.append("Muhammad Ali")

print(guests[0] + ", loved you in the Olympics, so please come to dinner.")
print(guests[1] + ", as Batman you are still invited to dinner.")
print(guests[2] + ", as my favorite Eagle, you are invited to dinner.")
print(guests[3] + ", as the director of Batman, you are invited to dinner.")
print(guests[4] + ", since I think you're awesome, can you please come to\
 dinner")
print(guests[5] + ", as the greatest, would you come to dinner?")