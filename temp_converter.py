print("In 1724, physicist Daniel Gabriel Fahrenheit proposed a temperature scale, the Fahrenheit scale.\n"
       "The Celsius scale is also a temperature scale which serves as an SI derived unit, and hence used worldwide.\n")
choice = int(input("Enter choice 1 or 2 :\n"
                     "1. Fahrenheit to Celsius\n"
                     "2. Celsius to Fahrenheit\n"))
if choice ==1:
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature: "+str(Fahrenheit)+"F = "+str((Fahrenheit-32)*(5/9))+"C")

elif choice ==2:
    Celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature: "+str(Celsius)+"C = "+str((Celsius*9/5+32))+"F")

else:
    print("You did not enter correctly")
