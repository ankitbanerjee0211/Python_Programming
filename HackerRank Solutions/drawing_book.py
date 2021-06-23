#!/bin/python3

import os
import sys

def pageCount(n, p):

    return int(min(p//2, n//2 - p//2))

        #     OR 

    # p_even = (p - p % 2)
    # n_even = (n - n % 2)
    # return int(min(p_even / 2, n_even/2 - p_even/2))

        # OR WE CAN USE 

    # p_even = (p - p % 2)
    # n_even = (n - n % 2)
    # pages = p_even / 2
    # pages_rev = (n_even - p_even)/2
    # min_pages = min(pages, pages_rev)
    # return int(min_pages)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()