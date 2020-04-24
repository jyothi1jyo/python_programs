SPEED_OF_LIGHT = 299792458
print("One of the exciting human discoveries is that mass and energy are interchangable and are related by the equation E = m × C^2. \n"
      "This relationship was uncovered by Albert Einstein almost 100 years ago.\n"
      "We now know that the sun produces its heat by transforming small amounts of mass into large amounts of energy.")
mass = float(input("Enter weight in kg: "))
print("E = m * c^2")
print("E = "+ str(mass))
print("c =" +str(SPEED_OF_LIGHT))
print(str(mass*(SPEED_OF_LIGHT**2))+"joules of energy")