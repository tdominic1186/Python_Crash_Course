# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:21:49 2018

@author: ACANTAMA
"""

#Starts with list of unconfirmed users and 
#an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
#Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())