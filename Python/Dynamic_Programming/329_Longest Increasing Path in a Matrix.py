class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}#i,j
        rows=len(matrix)
        cols=len(matrix[0])
        req=0
        def dfs(i,j,prev):
            if i<0 or j<0 or i==rows or j==cols or matrix[i][j]<=prev:
                return 0
            if (i,j)in dp:
                return dp[(i,j)]
            dp[(i,j)]=1
            dp[(i,j)]+=max(dfs(i+1,j,matrix[i][j]),dfs(i-1,j,matrix[i][j])
                          ,dfs(i,j+1,matrix[i][j]),dfs(i,j-1,matrix[i][j]))    
            return dp[(i,j)]
        for r in range(rows):
            for c in range(cols):                
                req=max(req,dfs(r,c,-1))
        return req