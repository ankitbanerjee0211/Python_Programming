import random

print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to the Guess My Number App  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

number = random.randint(1,20)
name = input("Hello! What is you name: ").title()
print("Well " + name + ", I am thinking of a number between 1 and 20.\n")
for i in range(5):
    guess = int(input("Take a guess: "))
    if guess > number:
        print("Your guess is too high.\n")
    elif guess < number:
        print("Your guess is too low.\n")
    elif guess == number and i == 0:
        print("\nGood job, {}! You guessed my number in only {} guess! You are awesome.".format(name, i+1))
        break
    elif guess == number and i > 0:
        print("\nGood job, {}! You guessed my number in {} guesses!".format(name, i+1))
        break
    if guess != number and i == 4:
        print("Game Over. The number I was thinking of was " + str(number) + ".")
