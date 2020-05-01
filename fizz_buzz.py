def main():
    print('In the game Fizz Buzz, players take turns counting up from one. If a player’s turn lands on a'
    "number that’s divisible by 3, she should say “fizz” instead of the number, and if it lands on a"
    "number that’s divisible by 5, she should say “buzz” instead of the number. If the number is both"
    'a multiple of 3 and of 5, she should say "fizzbuzz" instead of the number.')
    n = int(input("Number to count to : "))
    fizz_count,buzz_count=fizzbuzz(n)
    print("Fizz count is "+str(fizz_count))
    print("Buzz_count is "+str(buzz_count))


def fizzbuzz(n):
    temp = 1
    fizz_count=0
    buzz_count=0
    while(temp<=n):
        if (temp%5==0 and temp%3==0):
            print("fizzbuzz")
            fizz_count+=1
            buzz_count+=1
        elif (temp%3==0):
            print("fizz")
            fizz_count += 1
        elif (temp%5==0):
            print("buzz")
            buzz_count += 1
        else:
            print(temp)
        temp+=1
    return fizz_count,buzz_count




if __name__ == "__main__":
    main()
