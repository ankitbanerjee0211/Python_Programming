#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a_dist = abs(z - x)
    b_dist = abs(z - y)
    if a_dist > b_dist:
        s = 'Cat B'
    elif b_dist > a_dist:
        s = 'Cat A'
    else:
        s = 'Mouse C'
    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
