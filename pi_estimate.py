import random

PI = 3.14159265358979
# Number of digits after decimal point to be displayed
# Should be less than or equal to 14 for double precision float
DIGITS = 5
RADIUS = 1.0

def main():
    print("There are numerous ways to estimate the value of π: while advanced algorithms have computed up to 50 trillion digits of π (as of January 2020), there is also an extremely inefficient yet utmost astonishing method based on bouncing billiards."
            "A simple probabilistic approach is the so-called Monte Carlo method. As shown below, we have a circle with radius 1, enclosed by a 2 by 2 square. The area ratio of circle to square is π/4. We can then throw a pebble many times, which lands uniformly inside the square. The probability of landing inside the circle is hence π/4."
            "Your task is to write a program that asks a user for the number of throws (n), simulate pebble throwing, and lastly compute the number of times (m) the pebble lands inside the circle. You can then estimate π as 4m/n. As you expect, the estimated value becomes closer to the true value as the number of throws increases.")
    while True:
        num_trials = input('Number of trials (press Enter to quit): ')
        if num_trials == '':
            print('Program has ended.')
            break
        num_trials = int(num_trials)
        pi = estimate_pi(num_trials)
        print(f'Actual value of pi:  {PI:.{DIGITS}f}...')
        print(f'The estimated value: {pi:.{DIGITS}f}')


def estimate_pi(num_trials):
    count = 0
    for i in range(num_trials):
        x = random.uniform(-RADIUS, RADIUS)
        y = random.uniform(-RADIUS, RADIUS)
        if x*x + y*y < RADIUS*RADIUS:
            count += 1
    return 4.0 * count / num_trials


if __name__ == '__main__':
    main()
