#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    len_list = []
    len_list.append(len(arr))
    while arr != []:
        m = min(arr)
        for i in range(len(arr)):
            arr[i] -= m
        for j in range(len(arr)):
            if 0 in arr:
                arr.remove(0)
        len_list.append(len(arr))
    len_list.pop(-1)
    return len_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
