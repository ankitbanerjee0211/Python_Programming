'''
🐍🐍Python :>🐍🐍


🐍 Comment :

    Use # to comment out a line or u can use ctrl + / to serve the same purpose.

    Use ''' ''' to use multiline comment or multiline string

🐍Variable Name :

    Starts with underscore or letter

    Only contain alphanumeric characters

🐍Variable Transformation :

    e = int(e) to make integer

    e = float(e) to make float

    e = str(e) to make string

🐍 String function :

    line = "I am a {}.".format("boy")
    # no of the variables can be used e.g. 0,1,2,3,4.... In the {} according to the variable serials.
    noun = "boy"
    line2 = f"I am a {noun}."

    Use + operator to concatenate

    print(name[2:5])

    print(name.strip()) removes the white spaces in both sides.
    lstrip() and rstrip() for left and right side.

    print(len(name)) length

    name2 = name.lower()
    name3 = name.upper()
    string_name.capitalize()

    Replace -> name4 = name.replace("char to replace", "char to replace with")


🐍 Operators :

    +, -, /, *

    ** Exponential

    // Floor division

    % Remainder

🐍 List [ , , , , ,] :

    Superimpose-able -> lst[2] = 20 will replace the value
    Numbering of the elements start from 0

    lst.append(20) add to the last of the list
    lst.insert(2, 20) adds to the position 2

    lst.remove(element) removes the element from the list
    lst.pop() removes the last element
    del lst[3] to remove 3 positioned element from the list 
    del lst to delete the whole list and the list doesn't exist.
    lst.clear() to make the list an empty list.

🐍 Tuple ( , , , , ) :

    Elements are not replaceable

    list transformation : tpl = list(tpl)

    tuple transformation : lst = tuple(tpl)

🐍 Set { , , , , } :

    If u enter multiple duplicate entries in the set it just saves one. e.g. s1= set(4,5,3,3,3,3,2,2,2,1,1,1,7,1,9)
    print(s1) will print {1,2,3,4,5,7,9}.

    s1.add(444)
    s1.update(any list or any element) e.g. s1.update([12,23,44,77,99,5,47])

    s1.remove(element) if we know that the element is in the set.
    If we don't then use s1.discard(element) this will show no error message and execute the code.

    .pop(), .clear(), del, intersection, union can also be used.

'''


'''LIST'''

names = ['Ankit', 'Ayon', "Sarbo", "Roll no. "+str(55)]
for name in names:
    str1 = f"{name} is funny."
    # print(str1)


'''SET'''

s1 = {4,5,6,4,5,6,4,1,2,8,6,9,7,2,3,5,6,9,8,4,1,2,3,6,5,8,4,42,65}
s2 = {4,5,6,12,10,15,14,21,32,62,14,1,5,2,6,4,788,558,52,14,7,8}
# print(s1.union(s2))
# print(s1.intersection(s2))


'''DICTIONARY'''

ankitDict = {
    "Name": "Ankit",
    "Department": "ME",
    "Year": "1st",
    "YGPA": 9.00
}
# print(ankitDict)
# print(ankitDict["Name"], ankitDict["Year"])
ankitDict["YGPA"] = 9.83
# print(ankitDict)
ankitDict.popitem()
ankitDict.popitem()
# print(ankitDict) # del, clear, len also can be used
ankitDict.update({"Semester": "4th"})
# print(ankitDict)


'''BOOLEAN OPERATORS'''

a = True
b = False


'''CONDITIONAL OPERATORS'''

# age = input("Enter Your Age: ") # It is entered as a string value only
# print("Age: "+ age, type(age))
# age = int(input("Enter Your Age: ")) # Altered to integer
# print("Age:", age, type(age))
# if(age>18):
    # print("You can drive a car.")
# elif(age==18):
    # print("Go and grab a driving license. You can drive a car now.")
# else:
    # print("You can't drive a car.")


'''LOOPS'''

'''For Loop'''
# Print numbers between 1 to 1000
# for i in range(0, 1000): # range function used here
    # print(i+1)
# print(ankitDict)
# print("\n")
# for x in ankitDict:
    # print(x)
# print("\n")
# for y in ankitDict:
    # print(ankitDict[y])
# print("\n")
# for z in ankitDict.values():
    # print(z)
# print("\n")
# for p, q in ankitDict.items():
    # print(p, q)
# print("\n")
# print(ankitDict.items())
# print(type(ankitDict.items()))

'''While Loop'''
#  Printing 1 to 100
i = 0
while(i<100):
    # print(i+1)
    i+=1

'''Break and Continue Statement'''
# IF break statement is used then the iteration of the loop stops and got out of the loop/
# IF continue statement is used then the rest of the loop section is not executed but the iteration is continues.
i = 1
while(i<100):
    # print(i)
    if i == 5:
        i = 8
        continue
    if i == 78:
        break
    i+=1


'''*************FUNCTIONS*************FUNCTIONS*************FUNCTIONS**************'''

# def greet():
#     print("Good Morning sir!")
#     print("Good Morning ma'am!")
#     print("Good Morning kaka!")

# greet()

'''print("*****PROGRAM TO PRINT SUM OF n NUMBERS*****\n")
def greet():
    print("\t     Hello Sir/Madam!\n")
def sum(a, b):
    return a+b
greet()
n = int(input("Enter number of integers you want to add: "))
ans = input("\nIs there any floating point number? Y/N: ")
print("\n")
s = 0
if ans == "y" or ans == "Y":
    s = 0.0 # or we can use s = float(s)
for i in range(0, n):
    x = input(f"Enter no.{i+1} integer: ")
    if ans == "y" or ans == "Y":
        x = float(x)
    else:
        x = int(x)
    s = sum(s, x)
print("\n*****\tRunning Sum\t*****")
print("\nSum:", s)
print("\n")'''


'''*************CLASS*************CLASS*************CLASS**************'''

class Employee:
    def __init__(self, ename, esalary):
        self.name = ename
        self.salary = esalary

ankit = Employee("Ankit Banerjee", 45000)
arnab = Employee("Arnab Saha", 30000)
# print(ankit.name)
# print(arnab.salary)