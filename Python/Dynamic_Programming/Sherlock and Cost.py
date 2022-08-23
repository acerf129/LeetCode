#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    one,two=0,0
    for i in range(1,len(B)):
        tempa=max(two+abs(B[i-1]-1),one)
        tempb=max(two+abs(B[i]-B[i-1]),one+abs(B[i]-1))
        one=tempa
        two=tempb
    return max(one,two)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
