#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    '''
    A simple exercise is substrings. the first
    number must be type cast to compaire and change
    into military time.
    '''
    hour = int(s[0:2])
    rem = s[2:8]
    suf = s[8:10]
    if suf.upper() == 'PM' and hour != 12:
        hour += 12
    #have to convert 12am to 00
    elif suf.upper() == 'AM' and hour == 12:
        hour = 0
    #have to pad int < 10 with a zero
    return f"{hour:02d}{rem}"

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
