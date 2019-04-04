# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:38:49 2018

@author: ACANTAMA
"""

def favorite_book(title):
    """Prints a message that states the favorite title of the book that was passed in as the argument"""
    print("One of my favorite books is " + title.title() + ".")
    
favorite_book('a clockwork orange')