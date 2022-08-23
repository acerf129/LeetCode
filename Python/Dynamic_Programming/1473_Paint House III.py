class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        cache={}
        req=float('inf')
        def paint(i,j,k):
            if i==len(houses):
                if j==target:
                    return 0
                return req
            if j>target:
                return req
            if (i,j,k)in cache:
                return cache[(i,j,k)]
            mincost=req
            if houses[i]!=0:
                nei=j+(houses[i]!=k)
                mincost=min(mincost,paint(i+1,nei,houses[i]))
            else:
                for l in range(1,n+1):
                    nei=j+(l!=k)
                    curcost=cost[i][l-1]+paint(i+1,nei,l)
                    mincost=min(mincost,curcost)
            cache[(i,j,k)]=mincost
            return cache[(i,j,k)]
            
        req=paint(0,0,0)
        
        return req if req!=float('inf')else -1
        