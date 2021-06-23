print("|||  Welcome to the Favourite Teachers Program  |||\n")

fav_teachers = []
fav_teachers.append(input("Who is your first favourite teacher: ").title())
fav_teachers.append(input("Who is your second favourite teacher: ").title())
fav_teachers.append(input("Who is your third favourite teacher: ").title())
fav_teachers.append(input("Who is your fourth favourite teacher: ").title())

print("\nYour favourite teachers ranked are:", fav_teachers)
print("Your favourite teachers alphabetically are:", sorted(fav_teachers))
print("Your favourite teachers in reverse alphabetical order are:", sorted(fav_teachers, reverse=True))

print("\nYour top two favourite teachers are: " + " and ".join(fav_teachers[:2]) + ".")
print("Your next two favourite teachers are: " + " and ".join(fav_teachers[2:]) + ".")
print("Your last favourite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of {} favourite teachers.".format(len(fav_teachers)))

fav_teachers.insert(0, input("\nOops, {} is no longer your first favourite teacher. Who is your new FAVOURITE teacher: ".format(fav_teachers[0])).title())

print("\nYour favourite teachers ranked are:", fav_teachers)
print("Your favourite teachers alphabetically are:", sorted(fav_teachers))
print("Your favourite teachers in reverse alphabetical order are:", sorted(fav_teachers, reverse=True))

print("\nYour top two favourite teachers are: " + " and ".join(fav_teachers[:2]) + ".")
print("Your next two favourite teachers are: " + " and ".join(fav_teachers[2:4]) + ".")
print("Your last favourite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of {} favourite teachers.".format(len(fav_teachers)))

fav_teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())

print("\nYour favourite teachers ranked are:", fav_teachers)
print("Your favourite teachers alphabetically are:", sorted(fav_teachers))
print("Your favourite teachers in reverse alphabetical order are:", sorted(fav_teachers, reverse=True))

print("\nYour top two favourite teachers are: " + " and ".join(fav_teachers[:2]) + ".")
print("Your next two favourite teachers are: " + " and ".join(fav_teachers[2:]) + ".")
print("Your last favourite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of {} favourite teachers.".format(len(fav_teachers)))
