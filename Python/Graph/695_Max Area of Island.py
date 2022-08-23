class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        count=0
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            #base case return maxarea
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            req=1
            req+=dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)
            
            return req
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit or grid[r][c]==1:
                    count=max(count,dfs(r,c))
        return count