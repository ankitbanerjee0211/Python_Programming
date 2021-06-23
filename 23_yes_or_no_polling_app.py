import random

print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to the Yes or No Issue Polling App  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

issue = input("What is the yes or no issue you will be voting on today: ")
no_of_voters = int(input("What is the number of voters you will allow on the issue: "))
result_password = input("Enter a password for polling results: ")
vote_details = {}
yes_counter = 0
no_counter = 0

for i in range(no_of_voters):
    voter_name = input("\nEnter your full name: ").title()
    if voter_name not in vote_details:
        print("Here is our issue: " + issue)
        choice = input("What do you think...yes or no: ").lower()
        if choice == "yes" or choice == "no":
            vote_details[voter_name] = choice
            print("Thank you {}! Your vote of yes has been recorded.".format(voter_name))
        else:
            print("You have entered wrong option.")
    else:
        print("Sorry, it seems that someone with that name has already voted.")

print("\nThe following {} people voted:".format(len(vote_details)))
for voter in vote_details:
    print(voter)

print("\nOn the following issue: " + issue)
for key, value in vote_details.items():
    if value == "yes":
        yes_counter += 1
    else:
        no_counter += 1
if yes_counter > no_counter:
    print("Yes wins! {} votes to {}.".format(yes_counter, no_counter))
elif yes_counter < no_counter:
    print("No wins! {} votes to {}.".format(no_counter, yes_counter))
else:
    print("It's a tie! {} votes to {}.".format(no_counter, yes_counter))

password = input("\nTo see the voting results enter the admin password: ")
if password == result_password:
    for key,value in vote_details.items():
        print("Voter: {}\t\t\tVote: {}".format(key, value))
print("\nThank you for using the Yes or No Issue Polling App.")
