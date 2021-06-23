print("||| Welcome to the Grade Sorter App |||\n")

grades = []
grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

print("\nYour grades are:", grades)
grades = sorted(grades, reverse = True)
print("\nYour grades from highest to lowest are:", grades)
print("\nThe lowest two grades will now be dropped.")
for i in range(2,4):
    print("\nRemoved grade:", grades[i])
del(grades[-2:]) # OR WE CAN grades.pop() TWICE
print("\nYour remaining grades are:", grades)
print("Nice work!  Your highest grade is a " + str(grades[0]) + ".")
