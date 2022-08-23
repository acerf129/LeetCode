class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        check=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()
        req=0
        def dfs(i,j):
            if i<0 or j<0 or  i==rows or j==cols or grid[i][j]==-1 :
                return 0
            if len(visit)==rows*cols-check-1 and grid[i][j]==2:
                return 1            
            visit.add((i,j))
            val=0
            for dr,dc in directions:
                nr,nc =i+dr,j+dc
                if (nr,nc)not in visit:
                    val+=dfs(nr,nc)
            visit.remove((i,j))
            return val
        m,n=0,0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==-1:
                    check+=1
                if grid[i][j]==1:
                    m=i
                    n=j
        return dfs(m,n)
        