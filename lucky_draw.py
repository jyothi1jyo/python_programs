import random

def main():
    count = 0
    while True:
        name = input("Guest name (Press enter when done): ")
        if name == "":
            break
        count+=1
        if random.random() < 1/count:
            winner = name
    if count==0:
        print("No guests")
    elif count ==1:
        print(f'Only {winner} came so he/she is winner')
    else:
        print("Winner of the lucky draw is "+str(winner))



if __name__ == '__main__':
    main()
