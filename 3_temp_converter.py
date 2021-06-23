print("||| Welcome to the Temperature Conversion Program |||\n")
ftemp = float(input("What is the given temperature in degrees Fahrenheit: "))

ctemp = (ftemp - 32) * 5 / 9
ctemp = round(ctemp, 4)
ktemp = ctemp + 273.15
ktemp = round(ktemp, 4)

print("\nDegrees Fahrenheit:\t" + str(ftemp))
print("Degrees Celsius:\t" + str(ctemp))
print("Degrees Kelvin:\t\t" + str(ktemp))
