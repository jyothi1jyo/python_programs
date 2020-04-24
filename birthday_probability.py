DAYS_IN_A_YEAR = 365
print("Did you know that if 70 people are chosen at random, there's a 99.9% probability that at least two of them share a birthday?\n"
      "And in a random group of 23 people, there's a greater than 50% chance that two of them have the same birthday.\n"
      "Some people call it a paradox, but it's really just a surprising result of probability.\n")
people = int(input("How many people are there in the group? "))
if people < 1:
    print("You need atleast 2 people to make a group")
else:
    numerator = 1
    for p in range(0,people):
        term = 365 - p
        numerator*=term
    denominator = 365**people
    probability = round(((1 - (numerator / denominator)) * 100),2)
print("There is a "+str(probability)+"% chance at least two people share same birthday")