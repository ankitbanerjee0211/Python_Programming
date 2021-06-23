import cmath

print("|||  Welcome to the Quadratic Equation Solver App  |||\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

eq_number = int(input("How many equations would you like to solve today: "))

for i in range(eq_number):
    print("Solving equation #" + str(i+1))
    print("----------------------------------------------------------\n")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of a (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    print("\nThe solutions to {}x^2 + {}x + {} are: \n".format(a, b, c))

    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print("\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")
