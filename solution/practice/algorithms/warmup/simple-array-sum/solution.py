#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    '''
    trivial,  the solution is handed to us 
    in line 26, a more simple solution would be:
    >input()
    >print(sum(map(int, input().strip().split())))
    note: strip() is not required, just gets rid of 
    whitespace if present.
    '''
    answer = sum(ar)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

