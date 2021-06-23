print("||| Welcome to the MPH to MPS Conversion App |||\n")

mph = float(input("What is your speed in miles per hour: "))
mps = 1609 * mph/3600

# HERE WE USE ROUND FUNCTION
mps = round(mps, 2)
print("Your speed in meters per second is {}.".format(mps))

# OR WE COULD USE DECLARATIONS IN THE FORMAT FUNCTION

# {:.2f} # Upto 2 decimal number
