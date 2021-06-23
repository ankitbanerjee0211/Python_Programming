def format_address(address_string):
  # Declare variables
  house_num = ""
  street_name = []
  street = ""
  # Separate the address string into parts
  words = address_string.split()
  # Traverse through the address parts
  for word in words:
    # Determine if the address part is the
    # house number or part of the street name
    if word.isnumeric():
      house_num += word
    else:
      street_name.append(word)

  # Does anything else need to be done
  # before returning the result?
  # for i in range(1, len(streetname)+1):
  #   street = street_name
  street = " ".join(street_name)
  # Return the formatted string
  return "house number {} on street named {}".format(house_num, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
