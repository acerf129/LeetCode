class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        pre1,pre2=grid[0].copy(),grid[1].copy()
        for i in range(1,n):
            pre1[i]+=pre1[i-1]
            pre2[i]+=pre2[i-1]
            
        req=float('inf')
        for i in range(n):
            top=pre1[-1]-pre1[i]
            bot=pre2[i-1] if i>0 else 0
            second=max(top,bot)
            req=min(req,second)
        return req