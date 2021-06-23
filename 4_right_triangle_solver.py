import math

print("||| Welcome to the Right Triangle Solver App |||\n")
leg1 = float(input("What is the first leg of the triangle:\t"))
leg2 = float(input("What is the second leg of the triangle:\t"))

hp = math.sqrt(leg1**2 + leg2**2) # (leg1**2 + leg2**2)**(1/2)
area = (leg1 * leg2)/2

print("\nFor a triangle with leg of {} and {} the hypotenuse is {}.\nFor a triangle with leg of {} and {} the are is {}.".format(leg1, leg2, round(hp, 3), leg1, leg2, area))
