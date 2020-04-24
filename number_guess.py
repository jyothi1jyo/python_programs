import random

print("hello! Lets play a number guessing game. \n press ctrl+c to quit.")
name = str(input("Please enter your name: "))
number = random.randint(0,100)
print(name+", I'm thinking of an integer.")
valid = True
while valid:
    guess = int(input("Please enter your guess:"))
    if guess > number:
        print(name+", your guess was too high")
    elif guess < number:
        print(name+", your guess was too low")
    else:
        print("Congratulations"+ name+" you got it!")
        valid = False