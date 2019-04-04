# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:37:04 2018
p147
@author: ACANTAMA
"""

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)