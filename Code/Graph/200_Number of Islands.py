class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        rows=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(r,c):
            
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]=="0" or(r,c) in visit:
                return 0
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)   
            return 1
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit:
                    count+=dfs(r,c)
        return count