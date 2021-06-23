import random

print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to the Database Admin Program  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

log_on_information = {
    "gamer23":"Super12345",
    "sunday2":"sunnyleone35",
    "admin00":"admin1234",
    "ankit":"ankit12345"
}

username = input("Enter your username: ")

if username in log_on_information:
    password = input("Enter your password: ")
    if password == log_on_information[username]:
        print("\nHello " + username + "! You are logged in!")
        if username == "admin00":
            print("\nHere is the current user database: ")
            for key, value in log_on_information.items():
                print("\nUsername: {}\nPassword: {}".format(key, value))
        choice = input("\nWould you like to change your password: ").lower()
        if choice == "yes":
            new_password = input("\nWhat would you like your new password to be: ")
            if len(new_password) < 8:
                print("{} does not have minimum eight characters.")
            else:
                log_on_information[username] = new_password
        print("\n{} your password is {}.".format(username, log_on_information[username]))
    else:
        print("You have entered WRONG password.")
else:
    print("\nUsername not in database, goodbye.")
