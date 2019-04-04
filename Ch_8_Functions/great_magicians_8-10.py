"""
5/20/18
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase 'the Great' to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
p150
"""

def show_magicians(magician_names):
    """Prints the formatted names of a list of magicians"""
    for name in magician_names:
        print(name.title())

def formatted_magicians(magician_names):
    """Permanently formats the names of a list of magicians"""
    for name in range(len(magician_names)):
        magician_names[name] = magician_names[name].title()

def make_great(magician_names):
    """Permanently appends the phrase 'the Great' to each magician's name"""
    for name in range(len(magician_names)):
        magician_names[name] += ' the Great'


magician_names = ['houdini', 'david copperfield', 'david blaine']
great_names = []

print(magician_names)
show_magicians(magician_names)
formatted_magicians(magician_names)
make_great(magician_names)
print(magician_names)
show_magicians(magician_names)