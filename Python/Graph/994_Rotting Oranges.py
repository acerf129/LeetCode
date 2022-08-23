class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs
        req=deque()
        rows,cols=len(grid),len(grid[0])
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    req.append([r,c])
        if len(req)==0 or fresh==0:
            return 0
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        while req and fresh:
            for i in range(len(req)):
                r,c = req.popleft()
                for dr,dc in direction:
                    nr,nc=r+dr,c+dc
                    if nr<0 or nr==rows or nc<0 or nc==cols or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc]=2
                    req.append([nr,nc])
                    fresh-=1
            time+=1
                    
        return time if fresh==0 else -1