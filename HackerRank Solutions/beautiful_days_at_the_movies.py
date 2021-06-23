#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = list(range(i, j+1))
    count = 0
    for day in days:
        temp = day
        rev_day = 0
        while(day > 0):    
            Remainder = day % 10    
            rev_day = (rev_day * 10) + Remainder    
            day = day // 10
        day = temp
        val = abs(day - rev_day) / k
        if val == round(val):
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
