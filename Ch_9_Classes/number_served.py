''' 
Start with your program from Exercise 9-1 (page 166).

Add an attribute called number_served with a default value of 0. x

Create an instance called restaurant from this class. x

Print the number of customers the restaurant has served, and then change this value and print it again. x

Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. x

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. x
p171
'''

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

restaurant = Restaurant("the cheesesteak house", "american")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\nNumber Served: " + str(restaurant.number_served))
restaurant.number_served = 25
print("\nNumber Served: " + str(restaurant.number_served))

restaurant.set_number_served(30)
print("\nNumber Served: " + str(restaurant.number_served))

restaurant.increment_number_served(55)
print("\nNumber Served: " + str(restaurant.number_served))
