print("|||  Welcome to the Binary/Hexadecimal Converter App  |||\n")

max_value = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value + 1))
binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))

print("Generating lists....complete!\n")

print("Using slices, we will now show a  portion of each list.")
lower_range = int(input("What decimal number would you like to start at: "))
upper_range = int(input("What decimal number would you like to stop at: "))

print("\nDecimal values from {} to {}:".format(str(lower_range), str(upper_range)))
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from {} to {}:".format(str(lower_range), str(upper_range)))
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from {} to {}:".format(str(lower_range), str(upper_range)))
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("--------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" +  str(h))
