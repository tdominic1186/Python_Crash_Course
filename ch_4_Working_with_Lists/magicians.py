#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:47:39 2018

@author: Tony_MBP
"""
"""
defines list of magicians. then, for each variable in the list (to be stored 
temporarily in another variable known as 'magician'), I want you to print each 
name that was just stored as magician until the end of the list has been 
reached.

We begin by defining a list at line 1, just as we did in Chapter 3. At line 2,
we define a for loop. This line tells Python to pull a name from the list
magicians, and store it in the variable magician. At line 3 we tell Python to 
print the name that was just stored in magician. Python then repeats lines 2
and 3, once for each name in the list. It might help to read this code as
“For every magician in the list of magicians, print the magician’s name.”

basically, in a for/in stmt, you want to use the singular **for** (each item in 
the list) and plural for everything **in** (the list).

added newline outside of loop to break up program prints

"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print("\n-------")
    
"""
Same as above, but titles each name and adds text after each
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("\n-------")

"""
same as above, but adds another personalized stmt and creates a newline after
each iteration through the list.
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("\n-------")

"""
same as above, but adds another print stmt addressing everyone as it is outside
of the loop
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone. That was a great magic show!")
print("\n-------")

"""
debug space
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone. That was a great magic show!")
print("\n-------")