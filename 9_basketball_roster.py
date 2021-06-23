print("|||  Welcome to the Basketball Roster Program  |||\n")
player_positions = ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]
player_name = []
player_name.append(input("Who is your point guard: ").title())
player_name.append(input("Who is your shooting guard: ").title())
player_name.append(input("Who is your small forward: ").title())
player_name.append(input("Who is your power forward: ").title())
player_name.append(input("Who is your center: ").title())

print("\n\tYour starting 5 for the upcoming basketball season is")
for i in range(5):
    if i == 4:
        print("\t\t{}:\t\t\t\t{}".format(player_positions[i], player_name[i]))
    else:
        print("\t\t{}:\t\t\t{}".format(player_positions[i], player_name[i]))

print("\nOh no, {} is injured.".format(player_name[2]))
print("Your roster only has 4 players.")
player_name[2] = input("Who will take {}'s spot: ".format(player_name[2])).title()

print("\n\tYour starting 5 for the upcoming basketball season is")
for i in range(5):
    print("\t\t{}:\t{}".format(player_positions[i], player_name[i]))

print("\nGood luck {} you will do great!".format(player_name[2]))
print("Your roster has now 5 players.")
