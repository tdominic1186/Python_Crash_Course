#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:56:26 2018

@author: Tony_MBP
"""

"""
#creates alien_0 dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

#prints new points based on dictionary value
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#establishes starting x and y values for alien_0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
"""
#assigns keys and values to an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
"""
"""
#prints curren value for 'color' key
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

#changes color value to yellow in existing dictionary
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
"""


#prints original x position of alien_0
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

#move alien_0 to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
    
#The new posititon is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_position: " + str(alien_0['x_position']))







