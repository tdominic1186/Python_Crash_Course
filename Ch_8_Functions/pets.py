# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:48:39 2018

@author: ACANTAMA
"""
##positional argument
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#    
#describe_pet('hamster', 'harry')
##describe_pet('dog', 'willie')

#keyword argument
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#    
#describe_pet(animal_type='hamster', pet_name='harry')
#describe_pet(pet_name='harry', animal_type='hamster')

#default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name='willie')