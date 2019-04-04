#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:47:23 2018

@author: Tony_MBP
"""

guests = ['Christian Bale', 'Heath Ledger', 'Neil DeGrasse Tyson']

print(guests[0] + ", as Batman you are cordially invited to dinner.")
print(guests[1] + ", as the Joker, you can come to dinner but please behave.")
print(guests[2] + ", can you please come to dinner at my place?")
#heath ledger can't make it, he's deleted from the list
##chris nolan gets added to the list in his place
print("\nUnfortunately, " + guests[1] + " can't make it.")
del guests[1]
guests.insert(1, "Christopher Nolan")
#new invites
print("\n" + guests[0] + ", as Batman you are cordially invited to dinner.")
print(guests[1] + ", as Batman's director you can come to dinner instead of\
 Heath.")
print(guests[2] + ", can you please come to dinner at my place?")
#found a bigger table
print("\nEveryone, I found a bigger table!")
#added lol, bdawk, and ali to the guest list
guests.insert(0, "Lolo Jones")
guests.insert(2, "Brian Dawkins")
guests.append("Muhammad Ali")
#new invites
print("\n" + guests[0] + ", loved you in the Olympics, so please come to\
 dinner.")
print(guests[1] + ", as Batman you are still invited to dinner.")
print(guests[2] + ", as my favorite Eagle, you are invited to dinner.")
print(guests[3] + ", as the director of Batman, you are invited to dinner.")
print(guests[4] + ", since I think you're awesome, can you please come to\
 dinner")
print(guests[5] + ", as the greatest, would you come to dinner?")
#only a small table is available
print("\nUnfortunately, the table that I thought the restauraunt had reserved\
 was not actually reserved. I now only have space for two guests.")
#pop all except 2 guests from the list while printing a condolence to that
##guest
popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ", but there's just no room.")
popped_guest = guests.pop()
print("Apologies, " + popped_guest + ", but you just won't fit.")
popped_guest = guests.pop()
print("Hate to do this " + popped_guest + ", but you gotta go.")
popped_guest = guests.pop()
print(popped_guest + ", please don't hurt me, but you can't come to dinner\
 anymore.")

print("\nDon't worry " + guests[1] + ", you're Batman. I wasn't going to not\
 invite you.")
print("You too, " + guests[0] + ", of course you're still invited.")
#delete the last two guests and print to ensure the list is now empty
del guests[:]
print(guests)











