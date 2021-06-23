#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total_like = 0
    shared = 0

    for i in range(1, n+1):
        if i == 1:
            shared = 5
            liked = shared // 2
            total_like += liked
        else:
            shared = (shared // 2)*3
            liked = shared // 2
            total_like += liked

    return total_like

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
