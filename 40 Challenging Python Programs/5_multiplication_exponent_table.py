import math

print("||| Welcome to the Multiplication/Exponent Table App |||\n")
name = input("Hello, what is your name: ").title()
num = float(input("What number would you like to work with: "))
line = name + " Math is cool!"

print("\nMultiplication Table For " + str(num) + "\n")
for i in range(1, 10):
    print("\t{} * {} = {}".format(float(i), num, round(float(i)*num, 2)))

print("\nExponent Table For " + str(num) + "\n")
for j in range(1, 10):
    print("\t{} ** {} = {}".format(float(j), num, round(num**float(j), 2)))

print()
print(line)
print("\t" + line.lower())
print("\t\t" + line.title())
print("\t\t\t" + line.upper())
