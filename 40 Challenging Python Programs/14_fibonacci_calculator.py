import math

print("|||  Welcome to the Fibonacci Calculator App  |||\n")
num = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
terms = []
ratios = []
if num == 1:
    terms.append(float(1))
elif num >= 2:
    terms.append(float(1))
    terms.append(float(1))
    for i in range(3, num+1):
        term = float(terms[i-2]) + float(terms[i-3])
        terms.append(term)
print("The first {} numbers of the Fibonacci sequence are:".format(num))
for element in terms:
    print(int(element))

# term_1 = 1
# term_2 = 1
# print("The first {} numbers of the Fibonacci sequence are:".format(num))
# if num == 1:
#     print(term_1)
# if num >= 2:
#     print(term_1)
#     print(term_2)
#     for i in range(3, num+1):
#         term = term_1 + term_2
#         term_1 = term_2
#         term_2 = term
#         print(term)

print("\nThe corresponding Golden Ratio values are:")
for j in range(1, num):
    ratios.append(terms[j]/terms[j-1])
for ratio in ratios:
    print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; {:.3f}...".format(ratios[-1]))
