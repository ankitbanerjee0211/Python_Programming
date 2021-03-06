#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    for i in range(len(apples)):
        apples[i] += a
    for i in range(len(oranges)):
        oranges[i] += b
    for apple in apples:
        if apple >= s and apple <= t:
            apple_count += 1
    for orange in oranges:
        if orange >= s and orange <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
