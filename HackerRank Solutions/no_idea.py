# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
array = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# happiness = 0
# for num in array:
#     if num in a:
#         happiness += 1
#     elif num in b:
#         happiness -= 1
# print(happiness)
print(sum([(i in a) - (i in b) for i in array]))