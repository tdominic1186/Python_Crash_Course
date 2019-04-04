"""
5/21/18
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with 'the Great' added to each magician’s name.
p150
"""

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
    





def make_great(magician_names):
    """
    Creates a new list to hold each magician that has been made 'great'
    Appends 'the Great' to each magician's name
    Returns the modified names to the 'magician_names' list
    """
    # great_names = []


    while magician_names:
        name = magician_names.pop()
        great_name = name + ' the Great'
        great_names.append(great_name)

    # for great_name in great_names:
    #     magician_names.append(great_name)
    
    # return magician_names
        


magician_names = ['houdini', 'david copperfield', 'david blaine']
great_names = copy_list(magician_names)
#make_great(great_names)


print(magician_names)
print(great_names)

