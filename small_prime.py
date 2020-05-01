import time

UPPER_BOUND = 10000000  
PRIMES_TO_SHOW = 10

def main():
    print("This program will test whether a specified integer is prime.")
    print("It will also print out the " + str(PRIMES_TO_SHOW)
            + " primes <= the provided value.")
    print("For the sake of time, only numbers up to " + str(UPPER_BOUND)
            + " are allowed.")

    print("Calculating primes up to " + str(UPPER_BOUND) + ". Please wait...")
    primes = calculate_primes()

    while True:
        n = int(input("Please enter an integer in [0, " + str(UPPER_BOUND) + "]: "))

        # Check the primality of the provided value.
        prime = primes[n]

        if prime:
            print(str(n) + " is prime!")
        else:
            print(str(n) + " is not prime!")

        # Find the largest PRIMES_TO_SHOW <= n.
        to_show = last_n_primes(primes, n)
        print("The " + str(len(to_show)) + " primes <= " + str(n) + " are: ")
        print(to_show)
        print("")

def calculate_primes():
    # Initialize a list of size UPPER_BOUND + 1 to represent the integers in the
    # range [0, UPPER_BOUND].
    primes = [True] * (UPPER_BOUND + 1)

    # We know 0 and 1 are not prime so treat them as special cases.
    primes[0] = primes[1] = False

    # Keep track of time to display to the user later.
    start_time = time.time()

    # We only need to iterate up to the square root of n because the inner
    # loop starts at n^2.
    upper_bound = int(UPPER_BOUND**0.5)
    for i in range(2, upper_bound + 1):
        if primes[i]:
            # Cross out all numbers that are multiples of i starting at i^2
            for j in range(i * i, UPPER_BOUND + 1, i):
                primes[j] = False

    end_time = time.time()
    print("Calculated all primes up to " + str(UPPER_BOUND) + " in " 
            + str(end_time - start_time) + " seconds.")
    return primes

def last_n_primes(primes, n):
    show = []
    i = n
    # Start at n and work downward keeping track of primes.
    # Loop should also ensure we don't drop below zero.
    while len(show) < PRIMES_TO_SHOW and i >= 0:
        if primes[i]:
            show.append(i)
        i -= 1
    return show

if __name__ == "__main__":
    main()
