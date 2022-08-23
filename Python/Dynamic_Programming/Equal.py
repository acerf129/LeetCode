#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    minv=min(arr)
    req=float('inf')
    for i in range(5):
        total=0
        for n in arr:
            mv=minv-i
            diff=n-mv
            total+=diff//5
            total+=diff%5//2
            total+=diff%5%2
        req=min(req,total)
    return req
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
