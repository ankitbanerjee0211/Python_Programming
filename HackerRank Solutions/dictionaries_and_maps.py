# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {n:p for n,p in name_numbers}

while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name])) # New style of printing
        else:
            print('Not found')
    except:
        break