#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    x_list = list(range(1, len(p)+1))
    y_list = []
    for x in x_list:
        ind = p.index(x) + 1
        ind_y = p.index(ind) + 1
        y_list.append(ind_y)
    return y_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
