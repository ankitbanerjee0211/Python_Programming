print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to the Voter Registration App  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
name = input("Please enter your name: ").title()
age = int(input("Please enter your age: "))
if age < 18:
    print("\nYou are not old enough to register to vote.")
else:
    print("\nCongratulations {}! You are old enough to register to vote.\n".format(name))
    print("Here is a list of political parties to join.")
    for party in parties:
        print("\t\t- {}".format(party))
    print()

    your_party = input("What party do you like to join: ")
    if your_party.title() in parties:
        print("Congratulations {}! You have joined the {} party!".format(name, your_party))
        if your_party.title() == "Republican":
            print("That is a major party!")
        elif your_party.title() == "Democratic":
            print("That is a major party!")
        elif your_party.title() == "Independent":
            print("That is not a major party!")
        elif your_party.title() == "Libertarian":
            print("That is not a major party!")
        elif your_party.title() == "Green":
            print("That is not a major party!")
    else:
        print("\nYou didn't select a valid party.")
