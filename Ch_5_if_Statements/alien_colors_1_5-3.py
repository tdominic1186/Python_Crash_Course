#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:00:29 2018

test 1 pass with alien_color = 'green'

@author: Tony_MBP
"""

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

print("\n**********")

"""
test 2 fail with alien_color = 'yellow'
"""

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")