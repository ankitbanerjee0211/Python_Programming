#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    l = []
    while(n > 0):
        rem = n % 2
        l.insert(0, str(rem))
        n = n//2
    s = "".join(l)
    count = 0
    for part in s.split('0'):
        temp = len(part)
        if temp > count:
            count = temp
    print(count)