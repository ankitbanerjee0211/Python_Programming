#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    digits = [int(letter) for letter in str(n)]
    count = [1 for digit in digits if digit != 0 if n%digit == 0]
    return len(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        fptr.write(str(result) + '\n')

    fptr.close()