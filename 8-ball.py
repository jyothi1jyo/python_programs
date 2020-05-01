'''
The idea behind an 8-Ball is very simple. You ask the eight ball a yes or no question, and it tells
you the answer. Except, that the answer it choses is randomly selected from a set of prefabricated
responses. Write a program that continuously prompts the user for a yes or no question, and then randomly
selects from a set of canned answers

'''

import random

def main():
        responses = ["yes","no","May be","Ask again later","Better not tell you now","Cannot predict now",
                     "Concentrate and ask again","Don’t count on it","Most likely","Yes – definitely",
                     "Without a doubt","Signs point to yes","Reply hazy, try again","My reply is no",
                     "Outlook not so good","Outlook good","My sources say no","It is decidedly so"]
        while (True):
            question = input("Ask a yes or no question: ")
            if question=="":
                break

            response = random.randint(0,len(responses)-1)
            print(responses[response])

if __name__ == "__main__":
    main()
