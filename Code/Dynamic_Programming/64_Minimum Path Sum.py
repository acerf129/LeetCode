class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        rows,cols=len(grid),len(grid[0])
        def dfs(i,j):
            if (i==rows and j==cols-1) or (j==cols and i==rows-1):
                return 0
            if i==rows or j==cols:
                return float('inf')
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
            
            return dp[(i,j)]
        return dfs(0,0)