import random
import time

JACKPOT =100
WIN =10
LAG = 0.5

def main():
    print("Welcome to the Python Slot Machine.\nYou have been allotted 100 tokens to begin.\n"
            "To see your balance type 'b'. To spin the machine type 's' \n"
            "Additional help can be found by typing 'h'. Good luck!")
    tokens = 2
    while tokens>0:
        char = input(" > ")
        if char.lower()=='h':
            help()
        elif char.lower()=='b':
            print("Your current balance: "+str(tokens))
        elif char.lower() == 's':
            winnings = spin()
            tokens+= winnings
        elif char.lower() == 'e':
            print("You have exited the game ")
            exit(0)
    print("You are out of tokens")

'''
    This function converts shorthand commands to their full counterparts. It
    also removes extraneous capitalization and spacing.
   
    variable = variable.strip().lower()
'''
def spin():
    print("Spinning . . . ")
    time.sleep(LAG)
    one = int(random.randint(0,9))
    two = int(random.randint(0,9))
    three = int(random.randint(0, 9))
    print(one,end=" ",flush=True)
    time.sleep(LAG)
    print(two,end=" ", flush=True)
    time.sleep(LAG)
    print(three, flush=True)
    time.sleep(LAG)
    if one==two==three:
        print("Jackpot! 100 tokens")
        return JACKPOT
    elif one==two or two==three or three==one:
        print("You have won 10 tokens")
        return WIN
    else:
        print("you did not win anything")
        return -1



def help():
    print("Python Slot Machine manual")
    print("\t 'B' or 'b' \t -> print the user's current balance")
    print("\t 'S' or 's'  \t -> initiate a slot machine spin")
    print("\t 'H' or 'h'  \t -> print this information")
    print("\t 'E' or 'e'  \t -> exit the current session")



if __name__ == '__main__':
    main()
