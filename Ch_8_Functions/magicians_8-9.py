"""
5/20/18
p150
"""

def show_magicians(names):
    """Prints the names of a list of magicians"""
    for name in names:
        print(name.title())

magician_names = ['houdini', 'david copperfield', 'david blaine']

show_magicians(magician_names)
