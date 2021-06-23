print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to Shipping Accounts Program  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

users = ["ankit", "ajoy", "sayan", "babli", "sumit", "arnob"]

username = input("Hello, what is your username: ")
username = username.lower().strip()

if username in users:
    print("\nHello, {}. Welcome back to your account.".format(username))
    print("Current shipping prices are as follows:")

    print("\nShipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 101 to 500:\t\t$5.00 each")
    print("Shipping orders 501 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    quantity = int(input("\nHow many items would you like to ship: "))

    if quantity > 0 and quantity <= 100:
        price = 5.10
    elif quantity > 100 and quantity <= 500:
        price = 5.00
    elif quantity > 500 and quantity <= 1000:
        price = 4.95
    elif quantity > 1000:
        price = 4.80
    else:
        price = 0
        print("This is not a valid quantity")
        pass

    shipping_cost = quantity * price
    print("To ship {} items it will cost you ${} at ${} per item".format(quantity, round(shipping_cost, 2), price))

    choice = input("\nWould you like to place this order (y/n):").lower()
    if choice.startswith("y"):
        print("Okay. Shipping your {} items.".format(quantity))
    else:
        print("Okay. We are expecting next time.")

    print("Thank you for using our app.")
else:
    print("Sorry, you do not have an account with us. Goodbye.")
