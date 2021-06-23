print("|||           Summary Table           |||\n")

num_all = {}

num_all["num_string"] = ['15', '100', '55', '42']
num_all["num_ints"] = [15, 100, 55, 42]
num_all["num_floats"] = [2.2, 5.0, 1.245, 0.142857]
num_all["num_lists"] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(num_all)

for element, value in num_all.items():
    print("The variable {} is a".format(element), type(num_all[element]))
    print("It contains the elements: ", value)
    print("The element {} is a".format(value[0]), type(value[0]))
    print()

print("Now sorting num_string and num_ints...")
num_all["num_string"].sort()
print("Sorted num_string:", num_all["num_string"])
num_all["num_ints"].sort()
print("Sorted num_int:", num_all["num_ints"])

print("\n Strings are sorted alphabetically while integers are sorted numerically!")
