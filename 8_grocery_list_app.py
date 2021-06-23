import datetime

print("|||  Welcome to the Grocery List App  |||\n")

print("Current Date and Time:",datetime.datetime.now().strftime("%m/%d    %I:%M"))
# COULD HAVE DONE THIS
# time = datetime.datetime.now()
# month = str(time.month)
# day = str(time.day)
# hour = str(time.hour)
# minute = str(time.minute)

grocery_list = ['Meat', 'Cheese']
print("You currently have {} in your list".format(" and ".join(grocery_list)) + "\n")

for i in range(3):
    item = input("Type of food to add to the grocery list: ")
    grocery_list.append(item.title())

print("Here is your grocery list:\n", grocery_list)
grocery_list.sort()
print("Here is your grocery list sorted:\n", grocery_list)

print("\nSimulating grocery shopping...\n")
print("Current grocery list: {} items".format(len(grocery_list)) + "\n", grocery_list)
bought = input("What food did you just buy: ")
if bought:
    for item in grocery_list:
        if item.lower() == bought.lower():
            if bought.lower() == "meat":
                print("Sorry, the store is out of Meat.")
                grocery_list.remove(item)
                substitute = input("What food you like instead: ")
                grocery_list.append(substitute.title())
            else:
                print("Removing {} from list...".format(item))
                grocery_list.remove(item)
                print("\nCurrent grocery list: {}".format(len(grocery_list)) + "\n", grocery_list)
                bought = input("What food did you just buy: ")
print("Here is what remains on your grocery list:\n", grocery_list)
