#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:19:02 2018

@author: Tony_MBP
"""

teams = ['eagles', 'cowboys', 'redskins', 'giants']

print("There are " + str(len(teams)) + " teams in the NFC East.")
      
print("In alphabetical order, those teams are the " + str(sorted(teams)) + ".")
print("\n-----")

"""
Use a loop to clean up the above code.
"""

teams = ['eagles', 'cowboys', 'redskins', 'giants']

print("There are " + str(len(teams)) + " teams in the NFC East.")

teams = sorted(teams)

print("In alphabetical order, those teams are:")
for team in teams:
    print("The " + team.title())
      
print("\n")