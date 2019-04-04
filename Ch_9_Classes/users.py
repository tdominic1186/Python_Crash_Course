''' 
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user. 
'''

class User():

    def __init__(self, first_name, last_name, age, favorite_color, favorite_band):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.favorite_band = favorite_band

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + "'s age is " + str(self.age) + ". Their favorite color is " + self.favorite_color + " and their favorite band is " + self.favorite_band.title() + ".")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

jc = User("jessica", "colliver", 29, "purple", "nsync")
tc = User("tony", "cantamaglia", 32, "blue", "led zepellin")
cc = User("cooper", "cantamaglia", 10, "gray", "whatever dad likes")

jc.describe_user()
jc.greet_user()
tc.describe_user()
tc.greet_user()
cc.describe_user()
cc.greet_user()
