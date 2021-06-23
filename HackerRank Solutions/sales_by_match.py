#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_dict = {}
    count = 0
    for color_code in ar:
        if color_code in count_dict:
            count_dict[color_code] += 1
        else:
            count_dict[color_code] = 1
    for color, value in count_dict.items():
        if value >= 2:
            count += value // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()