

prompt = ("Enter a series of pizza toppings that you would like.")
prompt += ("\nEnter 'quit' when you are done or wish to exit pizza builder. ")
        
active = True
toppings = []
print("\n")
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        toppings.append(message)
        print("\nWe'll add " + message + " to the pizza.")
        print("Your list of toppings now includes: ")
        for topping in toppings:
            print("\t" + topping.title())
    print("\n")
            
        
        
      
            