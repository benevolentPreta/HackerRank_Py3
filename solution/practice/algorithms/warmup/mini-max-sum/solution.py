#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    '''
    The sum of 4 is total minus 1 element
    min is total minus max, and max is 
    total minus min. If run time doesn't matter
    you can shorten with:
    print(sum(arr) - max(arr), sum(arr), min(a))
    '''
    minN = arr[0]
    maxN = arr[0]
    total = arr[0]
    for i in range(1, len(arr)):
        total += arr[i]
        if arr[i] > maxN:
            maxN = arr[i]
        if arr[i] < minN:
            minN = arr[i]
        i += 1
    print(total - maxN, total - minN)
    pass


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

