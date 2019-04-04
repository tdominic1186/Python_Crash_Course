#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:58:03 2018

5-6 Stages of life - Write an if-elif-else chain that determines a person's
stage of life.

@author: Tony_MBP
"""

age = 65

if age < 2:
    print("You're a baby.")
elif age >= 2 and age < 4:
    print("You're a toddler.")
elif age >= 4 and age < 13:
    print("You're a kid.")
elif age >= 13 and age < 20:
    print("You're a teenager.")
elif age >= 20 and age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")
