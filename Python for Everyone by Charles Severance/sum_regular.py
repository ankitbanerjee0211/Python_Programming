import re

hand = open('regex_sum_734508.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for i in stuff:
        num = float(i)
        numlist.append(num)

print(int(sum(numlist)))
