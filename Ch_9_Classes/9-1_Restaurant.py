''' 
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
'''

class Restaurant():
    """A simple model for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant's name and cuisine type."""
        print("The restaurant's name is " + self.restaurant_name.title() + " and the cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Inidcates if the restaurant is open."""
        print(self.restaurant_name.title() + " is open!")

restaurant = Restaurant("the cheesesteak house", "american")
jess_restaurant = Restaurant("three margaritas", "mexican")
mike_restaurant = Restaurant("hibachi grill", "japanese")
tony_restaurant = Restaurant("sausages", "german")

# print("My restaurant's cuisine type is " + restaurant.cuisine_type.title() + ".")
# print("My restaurant's name is " + restaurant.restaurant_name.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()
jess_restaurant.describe_restaurant()
mike_restaurant.describe_restaurant()
tony_restaurant.describe_restaurant()
