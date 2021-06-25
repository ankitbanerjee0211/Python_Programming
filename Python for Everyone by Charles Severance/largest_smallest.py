largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        numv = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None :
        largest = numv
    elif numv>largest :
        largest = numv

    if smallest is None :
        smallest = numv
    elif numv<smallest :
        smallest = numv

print("Maximum is", largest)
print("Minimum is", smallest)
