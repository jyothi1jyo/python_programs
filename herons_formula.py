import math
print("There are many ways to find the area of a triangle.\n"
      " Using Heron's Formula, one can find the area using A = sqrt(s*(s-a)*(s-b)*(s-b)), where s represents the semiperimeter of the triangle, or half the perimeter.\n"
      " If two sides (a, b) and the angle between them (C) are given, the area can be found using the formula 1/2 * a * b * sin(C). \n"
      "There are many ways to calculate information about a triangle, but sometimes it requires quite a bit of busywork.")

print("Welcome to triangle calculator")
print("What information do you have on triangle?\n"
      "1. Length of all three sides\n"
      "2. Length of two sides and the angle between them")
option = int(input("Please choose 1 or 2: "))
a = float(input("Length of side 1: "))
b = float(input("Length of side 2: "))

if option==1:
    c = float(input("Length of side 3: "))
    perimeter = a+b+c
    s = perimeter/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

elif option==2:
    c = float(input("Angle between them in degree: "))

    # Convert into radians
    c = c * math.pi / 180

    #Law of Cosines
    c = math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(c)))

    perimeter = a+b+c
    area = 0.5 * a * b * c

print("Analysis of your triangle . . . ")
print("Side 1: "+str(a))
print("Side 2: "+str(b))
print("Side 3: "+str(c))
print("Perimeter: "+str(perimeter))
print("Area: "+str(area))