class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        cache={}
        def backtrack(i,j):
            #exception
            if i<0 or j<0 or i==rows or j==cols :
                return 0            
            if (i,j) in cache:
                return cache[(i,j)]
            down= backtrack(i+1,j)
            right=backtrack(i,j+1)
            diag=backtrack(i+1,j+1)
            cache[(i,j)]=0
            if matrix[i][j]=="1":
                cache[(i,j)]=1+min(down,right,diag)
            return cache[(i,j)]
        backtrack(0,0)
        return max(cache.values())**2