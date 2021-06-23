#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    best_record = 0
    worst_record = 0
    record = []
    for score in scores:
        if score > max_score:
            max_score = score
            best_record += 1
        elif score < min_score:
            min_score = score
            worst_record += 1
    record.append(best_record)
    record.append(worst_record)
    return record

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
