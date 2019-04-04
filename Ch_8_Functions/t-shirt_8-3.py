# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:45:43 2018

@author: ACANTAMA
"""

def make_shirt(size, message):
    """Prints size of shirt requested and message to be printed on shirt."""
    print("The size shirt you requested is " + size.title() + ".")
    print("The message to be printed on the shirt is '" + message.title() + "'.")
    
make_shirt('large', 'dogs dig the long walk')
make_shirt(message='dogs dig the long walk', size='large')

    
