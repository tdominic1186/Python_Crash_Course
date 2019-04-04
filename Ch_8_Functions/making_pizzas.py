'''
Importing modules
p155 
'''
''' 
Importing an entire module. Requires dot notation (module_name.function_name()) as this import type imports all functions within a module. 
'''
# import pizza_loop_pos_arb

# pizza_loop_pos_arb.make_pizza(16, 'anchovies')
# pizza_loop_pos_arb.make_pizza(12, 'mushrooms', 'sausage', 'extra cheese')

''' 
Importing specific functions. This approach negates need for dot notation syntax since module and functions
are already being specifically called out. 
Syntax for one specific function is: from module_name import function_name
Syntax for multiple functions is: from module_name import function_0, function_1, function_2
 '''
# from pizza_loop_pos_arb import make_pizza

# make_pizza(16, 'sausage')
# make_pizza(12, 'onions', 'pepperoni', 'potatoes') 

''' 
Using as to give a function an alias. Used if the imported function might conflict with an existing name
in your program or if the function name is too long. 
Syntax for aliasing a function is: from module_name import function_name as fn
'''
# from pizza_loop_pos_arb import make_pizza as mp

# mp(16, 'french fries')
# mp(12, 'beef', 'onions', 'mozarrella cheese')

''' 
Using as to give a module an alias. Used in order to call a module's functions more quickly. 
Syntax for aliasing a module is: import module_name as mn
'''
# import pizza_loop_pos_arb as p

# p.make_pizza(16, 'beef')
# p.make_pizza(12, 'onions', 'pepperoni', 'sausage')

''' Importing all functions in a module. This appraoch should not be used and is only included here to recognize in other people's code. 
'''
from pizza_loop_pos_arb import *

make_pizza(16, 'sausage')
make_pizza(12, 'pepperoni', 'mushrooms', 'beef')
