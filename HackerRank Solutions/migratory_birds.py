#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_dict = {}
    for bird in arr:
        if bird in bird_dict:
            bird_dict[bird] += 1
        else:
            bird_dict[bird] = 1

    highest = bird_dict[arr[0]]

    for bird, count in bird_dict.items():
        if count > highest:
            highest = count
    
    high_birds = [bird for bird, count in bird_dict.items() if count == highest]

    high_birds.sort()
    
    return high_birds[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
