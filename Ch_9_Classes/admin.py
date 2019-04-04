"""
9-7. Admin: 

An administrator is a special kind of user. 

Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). x

Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. x

Write a method called show_privileges() that lists the administrator’s set of privileges. x

Create an instance of Admin, and call your method. x

p178
"""

class User():

    def __init__(self, first_name, last_name, age, favorite_color, favorite_band):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.favorite_band = favorite_band

    def describe_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title() + "'s age is " + str(self.age) + ". Their favorite color is " + self.favorite_color + " and their favorite band is " + self.favorite_band.title() + ".")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!")

class Admin(User):
    """Represents aspects of a User, specific to an Admin."""

    def __init__(self, first_name, last_name, age, favorite_color, favorite_band):
        """
        Initializes attributes of the parent class.
        Then initializes attributes specifici to an Admin.
        """
        super().__init__(first_name, last_name, age, favorite_color, favorite_band)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin privileges currently include: ")
        for privilege in self.privileges:
            print("- " + privilege.title())

tony = Admin('tony', 'cantamaglia', 32, 'blue', 'led zeppellin')
tony.describe_user()
tony.greet_user()
tony.show_privileges()
