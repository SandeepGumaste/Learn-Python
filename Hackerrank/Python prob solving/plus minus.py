import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x = 0
    y = 0
    z = 0
    for i in arr:
        if i > 0:
            x+=1
        elif i < 0:
            y+=1
        else:
            z+=1
    x = float(x)/n
    y = float(y)/n
    z = float(z)/n
    print(x)
    print(y)
    print(z)
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)