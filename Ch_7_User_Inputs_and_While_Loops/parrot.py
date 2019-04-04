# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:16:25 2018

@author: ACANTAMA
"""

# message = input("Tell me something and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# message = ""
# while message != 'quit':
# 	message = input(prompt)
	
	# if message != 'quit':
	# 	print(message)