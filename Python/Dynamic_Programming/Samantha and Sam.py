#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    mod=(10**9+7)
    req=0
    prev=0
    for i in range(len(n)):
        temp=prev*10+(i+1)*int(n[i])
        req=(req+temp)%mod
        prev=temp%mod
    return req%mod
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
