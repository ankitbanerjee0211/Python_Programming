import random

print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to a Game of Rock, Paper, Scissors  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

choices = ["rock", "paper", "scissors"]
rounds = int(input("How many rounds you like to play: "))
player_points = 0
comp_points = 0

for round in range(rounds):
    print("\nRound " + str(round + 1))
    print("Player: {}\tComputer: {}".format(player_points, comp_points))
    choice = input("Time to pick...rock, paper, scissors: ").lower()
    comp_rand = random.randint(0, 2)
    comp_choice = choices[comp_rand]
    if choice in choices:
        if choice == comp_choice:
            print("\t\tComputer: " + choice)
            print("\t\tPlayer: " + choice)
            print("\t\tIt is a tie, how boring!\n\t\tThis round was a tie.")
        elif comp_choice == "rock" and choice == "paper":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            player_points += 1
            print("\t\tPaper covers rock!")
            print("\t\tYou win round {}.".format(round+1))
        elif comp_choice == "paper" and choice == "rock":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            comp_points += 1
            print("\t\tPaper covers rock!")
            print("\t\tComputer wins round {}.".format(round+1))
        elif comp_choice == "scissors" and choice == "paper":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            comp_points += 1
            print("\t\tScissors cut paper!")
            print("\t\tComputer wins round {}.".format(round+1))
        elif comp_choice == "paper" and choice == "scissors":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            player_points += 1
            print("\t\tScissors cut paper!")
            print("\t\tYou win round {}.".format(round+1))
        elif comp_choice == "rock" and choice == "scissors":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            comp_points += 1
            print("\t\tRock crushes scissors!")
            print("\t\tComputer wins round {}.".format(round+1))
        elif comp_choice == "scissors" and choice == "rock":
            print("\t\tComputer: " + comp_choice)
            print("\t\tPlayer: " + choice)
            player_points += 1
            print("\t\tRock crushes scissors!")
            print("\t\tYou win round {}.".format(round+1))
    else:
        print("\t\tThat is not a valid game option!")
        print("\t\tComputer gets the point!")

print("\nFinal Game Results")
print("\t\tRounds Played: {}".format(rounds))
print("\t\tPlayer Score: {}".format(player_points))
print("\t\tComputer Score: {}".format(comp_points))
if player_points == comp_points:
    print("\t\tIt's a tie. We got no winners.")
elif player_points < comp_points:
    print("\t\tWinner: Computer :-(")
else:
    print("\t\tWinner: You :-)")
