import math

print("|||  Welcome to the Factorial Calculator App  |||\n")
num = int(input("What number would you like to compute the factorial of? "))
factorial = 1
print(str(num) + "! = ", end = "")
for i in range(1, num+1):
    print(str(i), end="")
    if i != num:
        print("*", end="")

print("\n\nHere is the result from the math library:")
print("The factorial of {} is {}!".format(num, math.factorial(num)))

print("\nHere is the result from my own algorithm:")
for i in range(1, num+1):
    factorial *= i
if num == 0:
    facorial = 1

print("The factorial of {} is {}!".format(num, factorial))

print("\nIt is shown twice that {}! = {} (with excitement)".format(num, factorial))
