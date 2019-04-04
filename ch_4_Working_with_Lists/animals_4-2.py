#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:04:19 2018

@author: Tony_MBP
"""
"""
create a list of animals with similar traits and use a for loop to print the
name of each animal.
"""
dogs = ['chocolate lab', 'golden retriever', 'jack russell terrier']

for dog in dogs:
    print(dog.title())
print("\n-----")

"""
same as above, but also print a personalized statement about each animal
"""

dogs = ['chocolate lab', 'golden retriever', 'jack russell terrier']

for dog in dogs:
    print("A " + dog.title() + " would make a great pet.")
print("\n-----")

"""
same as above with a stmt about what these animals have in common.
"""

dogs = ['chocolate lab', 'golden retriever', 'jack russell terrier']

for dog in dogs:
    print("A " + dog.title() + " would make a great pet.")
print("\nIn general, all types of dogs make great pets.")
print("\n-----")