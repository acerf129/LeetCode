#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque,defaultdict,Counter
#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def kingdomDivision(n, roads):
    # Write your code here
    #topological sort deque
    edges=defaultdict(set)
    degree=Counter()
    mod=(10**9+7)
    for r in roads:
        edges[r[0]].add(r[1])
        edges[r[1]].add(r[0])
        degree[r[0]]+=1
        degree[r[1]]+=1
    count={u:{True:1,False:1}for u in degree}
    leaves=deque([u for u in degree if degree[u]==1])
    root=0
    while True:
        node=leaves.popleft()
        #if node diff exclude all child diff
        count[node][False]=count[node][True]-count[node][False]
        if not degree[node]:
            root=node
            break
        else:
            parent=edges[node].pop()
            edges[parent].discard(node)
            degree[parent]-=1
            if degree[parent]==1:
                leaves.append(parent)
            count[parent][True]*=count[node][True]+count[node][False]
            count[parent][False]*=count[node][False]
    total=2*count[root][0]
    return(total%mod)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
