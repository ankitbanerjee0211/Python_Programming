print("|||  Welcome to the Average Calculator App  |||\n")

name = input("What is your name: ")
num = int(input("How many grades would you like to enter: "))
grade_list = []
for i in range(num):
    grade_list.append(float(input("Enter grade: ")))

grade_list = sorted(grade_list, reverse=True)

print("\nGrades Highest to Lowest:")
for grade in grade_list:
    print("\t\t" + str(round(grade)))

print("\n{}'s Grade Summary: ".format(name))
print("\t\tTotal Number of Grades:" + str(num))
print("\t\tHighest Grade:" + str(round(grade_list[0])))
print("\t\tLowest Grade:" + str(round(grade_list[-1])))
average = sum(grade_list)/len(grade_list)
print("\t\tAverage:" + str(round(average, 1)))

d_average = float(input("\nWhat is your desired average: "))
next_grade = d_average*(len(grade_list)+1) - sum(grade_list)
print("\nGood luck {}!".format(name))
print("You will need to get a {} on your next assignment to earn a {} average.".format(round(next_grade, 1), round(d_average, 1)))

print("\nLets see what your average could have been if you did better/worse on an assignment.")
changed_grade = float(input("What grade would you like to change: "))
new_grade = float(input("What grade would you like to change {} to: ".format(round(changed_grade))))
grade_list.insert(grade_list.index(changed_grade), new_grade)
grade_list.remove(changed_grade)

grade_list = sorted(grade_list, reverse=True)
print("\nNew Grades Highest to Lowest:")
for grade in grade_list:
    print("\t\t" + str(round(grade)))

print("\n{}'s New Grade Summary: ".format(name))
print("\t\tTotal Number of Grades:" + str(num))
print("\t\tHighest Grade:" + str(round(grade_list[0])))
print("\t\tLowest Grade:" + str(round(grade_list[-1])))
new_average = sum(grade_list)/len(grade_list)
print("\t\tAverage:" + str(round(average, 1)))

print("\nYour new average would be a {} compared to your real average of {}!".format(round(new_average, 1), round(average, 1)))
print("That is a change of {} points!".format(round(new_average - average, 1)))

print("\nToo bad your original grades are still the same!")
print(grade_list)
print("You should go ask for extra credit!")
