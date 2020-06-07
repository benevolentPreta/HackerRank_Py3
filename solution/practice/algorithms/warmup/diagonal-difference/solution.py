#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    '''
    matrix is always odd, square dimention,
    so we can use dist = #rows = len(arr),
    reading array is stored as a list of rows (lists)
    so we can read each row add one diagnal and subtract
    the other. the position of the left diagnal is always 
    i+1 for the next, and the right diagnal is always 
    dist - (i - 1)
    '''
    fSum = 0
    dist = len(arr)
    #col = len(arr[0])
    for i in range(dist):
        row = arr[i]
        fSum += row[i] - row[dist - i - 1]
    return abs(fSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
gutted, readable, simplified version of this code is:
>N = int(input())
>sum = 0
>for i in range(N):
>    row = list(map(int, input().split()))
>    sum += row[i] - row[N - i - 1]
>print(abs(sum))
'''
