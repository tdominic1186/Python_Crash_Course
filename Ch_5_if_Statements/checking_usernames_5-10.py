#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:19:36 2018

Checking usernames: create a progrma that simulates how websites ensure that everyone has a unique username.
Ensure that comparison is case insensitive ie if 'john' already exists, then 'JOHN' or 'JoHn' etc can't also be used.

@author: Tony_MBP
"""

current_users = ['jbird', 'tdominic1186', 'sk8erboi69', 'terry45', 'coopercity']
new_users = ['jbird', 'tdominic1186', 'jrpbball', 'kptemplin', 'drewbabez']

#used list comprehension to take the existing lists and apply a method that ensured all the users in the respective lists were lowercased before running the comparison loop.
#this creates case insensitivity to compare two lists

new_users = [new_user.lower() for new_user in new_users]
current_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(new_user + ' will need to enter a new username.')
    else:
        print(new_user + ' is available as a username.')
