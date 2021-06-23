print("||| Welcome to the Letter Counter App |||\n")

name = input("What is yout name:").title()
print("Hello " + name + "!")
print("I will count the number of times that a specific letter occur in a message. \n")

message = input("Please enter a message: ")
letter = input("Which letter you like to count the occurrences of: ")
count = 0

message = message.lower()
letter = letter.lower()

for character in message:
    if character == letter:
        count += 1

# OR WE COULD USE THE INBUILT COUNT FUNCTION

letter_count = message.count(letter)

print("\n{}, your message has has {} {}'s in it.".format(name, str(count), letter))
print("\n{}, your message has has {} {}'s in it.".format(name, str(letter_count), letter))
