#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:29:43 2018

Hello admin

@author: Tony_MBP
"""

usernames = ['jbird', 'tdominic1186', 'sk8erboi69', 'admin', 'coopercity']

for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")