"""
9-6. Ice Cream Stand:

An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). 

Either version of the class will work; just pick the one you like better. 

Add an attribute called flavors that stores a list of ice cream flavors. x

Write a method that displays these flavors. x

Create an instance of IceCreamStand, and call this method. x

p178
"""

class Restaurant():
    """A simple model for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant's name and cuisine type."""
        print("\nThe restaurant's name is " + self.restaurant_name.title() + " and the cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Inidcates if the restaurant is open."""
        print(self.restaurant_name.title() + " is open!")

    def set_number_served(self, customer_number):
        """Set number of customers that have been served."""
        self.number_served = customer_number

    def increment_number_served(self, additional_customers):
        """Add the given amount of customers to the Number Served"""
        self.number_served += additional_customers

class IceCreamStand(Restaurant):
    """
    Represents aspects of a restaurant, specific to an Ice Cream Stand.
    """
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initializes attributes of the parent class.
        Then initializes attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Prints list of flavors"""
        print("\nWe have the following flavors available: ")
        for flavor in self.flavors:
            print("- " + flavor.title())
    
coldcone = IceCreamStand('coldcone', 'ice cream')
coldcone.flavors = ['vanilla', 'chocolate', 'neopolitan']

coldcone.describe_restaurant()
coldcone.show_flavors()
