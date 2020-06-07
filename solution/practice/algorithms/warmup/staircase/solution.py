#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    '''
    Ah, brings me back to my CS135 days,
    trivial solution:
    >space = n - 1
    >pound = 1
    >line = ""
    >for i in range(n):
    >    line=""
    >    for j in range(space):
    >        line+= " "
    >        for k in range(pound):
    >            line+="#"    
    >        space -= 1
    >        pound += 1
    >        print(f"{line}")
    A more elegant solution would be:
    '''
    for i in range(n):
        print(' ' * (n - i - 1) + '#' * (i + 1))

if __name__ == '__main__':
    n = int(input())

    staircase(n)

