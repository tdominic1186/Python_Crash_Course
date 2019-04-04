"""
9-8. Privileges: 

Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. x

Move the show_privileges() method to this class. x

Make a Privileges instance as an attribute in the Admin class. x

Create a new instance of Admin and use your method to show its privileges. 

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

class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin privileges currently include: ")
        for privilege in self.privileges:
            print("- " + privilege.title())


class Admin(User):
    """Represents aspects of a User, specific to an Admin."""

    def __init__(self, first_name, last_name, age, favorite_color, favorite_band):
        """
        Initializes attributes of the parent class.
        Then initializes attributes specific to an Admin.
        """
        super().__init__(first_name, last_name, age, favorite_color, favorite_band)
        self.privileges = Privileges()

    

tony = Admin('tony', 'cantamaglia', 32, 'blue', 'led zeppellin')
tony.describe_user()
tony.greet_user()
tony.privileges.show_privileges()
