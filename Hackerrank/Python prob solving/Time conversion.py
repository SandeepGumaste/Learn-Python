#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h = int(s[:2])
    
    if "AM" in s:
        if h == 12:
            h = "00"
            s = h + s[2:-2]
            return (s)
        else:
            return s.replace("AM","")
    else:
        if h == 12:
            return s.replace("PM","")
        else:
            h += 12
            return str(h) + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(str(result) + '\n')

    f.close()
