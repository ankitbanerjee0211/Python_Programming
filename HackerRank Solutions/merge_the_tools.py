def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    s_list = []
    length = n//k

    for i in range(length):
        s_list.append(string[i * (n//length) : n//length + i * (n//length)])

    for string in s_list:
        temp_s = ""
        for letter in string:
            if letter not in temp_s:
                temp_s += letter
        print(temp_s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)