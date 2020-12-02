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
    x = 0
    m = len(arr)-1
    y = list()
    z = list()
    for i in range(len(arr)):
        y.append(arr[x][x])
        z.append(arr[x][m])
        x +=1
        m -=1
    return abs(max(sum(y),sum(z)) - min(sum(y),sum(z)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()