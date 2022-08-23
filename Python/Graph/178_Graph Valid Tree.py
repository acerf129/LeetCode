from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        preMap={i:[]for i in range(n)}
        visit=set()
        for pre,cur in edges:
            preMap[pre].append(cur)
            preMap[cur].append(pre)
        
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for j in preMap[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True


        return dfs(0,-1) and n==len(visit)