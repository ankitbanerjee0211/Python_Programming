#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap = 0
    days_before_sept = 0
    date = ''
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            leap = 1
    elif year >= 1919 and year <= 2700:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = 1
        elif year % 4 == 0:
            leap = 1
    if leap == 1:
        days_before_sept = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
    else:
        days_before_sept = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    sept_day = 256 - days_before_sept
    if year == 1918:
        sept_day += 13
    date += str(sept_day) + '.09.' + str(year)
    return date
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
