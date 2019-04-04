 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:59:17 2018

@author: Tony_MBP
"""
"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""

#make an empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
#changes attributes of the first three aliens 
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points']= 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
    
#show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))