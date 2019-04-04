def show_magicians(magician_names):
    """
    Prints the formatted names of a list of magicians
    """

    while magician_names:
        for magician_name in magician_names:
            magician_name = magician_names.pop()
            print(magician_name.title())

def copy_list(magician_names):
    """
    Makes a copy of list 'magician_names'
    """

    clone = magician_names[:]
    return clone


magician_names = ['houdini', 'david copperfield', 'david blaine']
great_names = copy_list(magician_names)

print(magician_names)
print(great_names)
