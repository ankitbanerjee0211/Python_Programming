# Enter your code here. Read input from STDIN. Print output to STDOUT
t  = int(input())
s_list = []
for i in range(t):
    s_list.append(input())
for string in s_list:
    s_even = ""
    s_odd = ""
    for i in range(len(string)):
        if i % 2 == 0:
            s_even += string[i]
        else:
            s_odd += string[i]
            
    s = s_even + " " + s_odd
    print(s)
