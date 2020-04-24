from math import sqrt
count = 0
print("Welcome to quadratic equation solver !")
print("This program will solves equations of form Ax^2 + Bx + c = 0.")
A = float(input("Enter the coefficient for A: "))
B = float(input("Enter the coefficient for B: "))
C = float(input("Enter the coefficient for C: "))
print("The roots of "+str(A)+"x^2 + "+str(B)+"x + "+str(C)+" =0 are:")

descriminant = (B ** 2) - (4 * A * C)
if descriminant < 0:
    descriminant = abs(descriminant)
    count = 1
x=(-B/(2*A))
y=sqrt(descriminant)/(2*A)
if count ==1:
    print("x1 = " + str(x)+" + i"+str(y))
    print("x2 = " + str(x) + " - i" + str(y))
else:
    x1 = x+y
    x2 = x-y
    print("x1 = "+str(x+y))
    print("x2 = "+str(x-y))

