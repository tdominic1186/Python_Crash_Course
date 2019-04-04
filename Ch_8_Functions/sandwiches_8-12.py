''' 
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time. 
p 154
'''

def make_sandwich(*ingredients):
    ''' Summarize the sandwich we are about to make. '''
    print('\nMaking a sandwich with the following ingredients:')
    for ingredient in ingredients:
        print("- " + ingredient)
    
make_sandwich('lettuce', 'tomato', 'onion', 'salami')
make_sandwich('roast beef', 'provolone cheese', 'onion')
make_sandwich('meatballs', 'mozzarella cheese')
