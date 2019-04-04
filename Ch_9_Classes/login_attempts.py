"""
9-5. Login Attempts: 

Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). x

Write a method called increment_login_attempts() that increments the value of login_attempts by 1. x

Write another method called reset_login_attempts() that resets the value of login_attempts to 0.x

Make an instance of the User class and call increment_login_attempts()
several times. x

Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). x

Print login_attempts again to make sure it was reset to 0.x
p171
"""

class User():

    def __init__(self, first_name, last_name, age, favorite_color, favorite_band):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.favorite_band = favorite_band
        self.login_attempts = 0

    def describe_user(self):
        """Describes user's attributes."""
        print(self.first_name.title() + " " + self.last_name.title() + "'s age is " + str(self.age) + ". Their favorite color is " + self.favorite_color + " and their favorite band is " + self.favorite_band.title() + ".")

    def greet_user(self):
        """Greets user by formatted first and last name."""
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Increments login_attempts from the user by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0

jc = User("jessica", "colliver", 29, "purple", "nsync")

jc.increment_login_attempts()
jc.increment_login_attempts()
jc.increment_login_attempts()
jc.increment_login_attempts()
print("\nThe number of times user has attempted to log in: " + str(jc.login_attempts))

jc.reset_login_attempts()
print("\nThe number of times user has attempted to log in: " + str(jc.login_attempts))