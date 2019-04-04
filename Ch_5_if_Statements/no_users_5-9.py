#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:14:01 2018

check for an empty list (no users)
commented out the empty list (line 13)

@author: Tony_MBP
"""

usernames = ['jbird', 'tdominic1186', 'sk8erboi69', 'admin', 'coopercity']
#usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username + ", would you like to see a status report?")
        elif username!= 'admin':
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")