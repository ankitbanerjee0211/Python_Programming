#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    tp = len(s) - m + 1 #total number of pieces possible
    ways = 0
    for i in range(tp):
        if sum(s[i : i+m]) == d:
            ways += 1
    return ways

    # tp = len(s) - m + 1 #total number of pieces possible
    # return len([1 for i in range(tp) if sum(s[i:i+m])==d])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()