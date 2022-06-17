name= input('Hi! Welcome. What is your name?')
print ('Hi ' + name)

#format string or f string
print (f"How old are you {name}?") 
guess= input(f"How old am I do you think?")


my_age=26
if guess > my_age :
    print ("Nahh... lower")
else :
    print ("Perhaps higher")
print (f"Yay. You guessed it. I'm {my_age}")
