"""
Passing an Arbitrary Number of Arguments
p 151
"""

def make_pizza(*toppings):
    """
    Print the list of toppings of the pizza being made.
    """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')