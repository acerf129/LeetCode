class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        28-6*2
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 1
            if (i,j)in visit:
                return 0
            visit.add((i,j))
            req=0
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                req+=dfs(nr,nc)
            return req
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    return dfs(r,c)