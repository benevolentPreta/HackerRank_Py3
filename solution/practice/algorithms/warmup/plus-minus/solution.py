#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    '''
    There is probably a better solution than this
    but this would be the trivial solution, and it 
    is successful.
    '''
    pos, neg, zero = 0, 0, 0
    size = len(arr)
    for i in range(size):
        if arr[i] > 0:
            pos+=1
        elif arr[i] < 0:
            neg+=1
        else:
            zero+=1
    print(float((pos/size)))
    print(float((neg/size)))
    print(float((zero/size)))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

