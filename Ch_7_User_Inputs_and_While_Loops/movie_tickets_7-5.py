

prompt = ("Enter your age to find out your ticket price. ")
prompt += ("\nEnter 'quit' if you wish to end the program. ")


active = True


while active:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        price = 0
    elif int(age) < 12:
        price = 12
    elif int(age) >= 12:
        price = 15
    print("The price for your ticket is $" + str(price) + ".")






