"""
using break to exit a loop
"""

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        print("Fuck you then.")
        break
    else:
        print("I'd love to to " + city.title() + "!")


