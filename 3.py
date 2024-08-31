import random
name = (input("Hello, what's your name? "))
secret = random.randint(1, 10)
print ("Hi" + " "+str(name) + ", I'm thinking of a number betwween 1 and 10.")
guess = int(input("Enter a number betvween 1 and 10: "))
if guess == secret:
    print ("Wow, you won!")
else:
    print ("You lost. Better luck next time. The right number was, " + str(secret))