#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    '''
    Three conditions to satify:
    All bugs have a pair and either:
    bugs are already in order, or a space exists
    '''
    n = len(b)
    # check if a hole is present in the string
    hole = '_' in b
    # all ladybugs need atleast one match
    for i in range(n):
        if b[i] != '_' and b.count(b[i]) == 1:
            return 'NO'
        # if all bugs have pairs, and a hole exist, can be solved
    if hole:
        return 'YES'
        # if no hole exists, bugs must be in order
        # check first, and last pairs first, then rest
    for k in range(n):
        if (k == 0 and b[k] != b[k+1]) or (k == n-1 and b[k] != b[k-1]) or (b[k] != b[k-1] and b[k] != b[k+1]):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
