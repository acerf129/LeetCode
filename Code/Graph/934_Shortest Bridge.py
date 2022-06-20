class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        req=float('inf')
        length=len(grid)
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def invalid(r,c):
            return r<0 or c<0 or r==length or c==length 
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or(r,c)in visit:
                return 
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            return
        def bfs():
            res,queue=0,deque(visit)            
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    for dr,dc in directions:
                        cr,cc=r+dr,c+dc
                        if invalid(cr,cc) or (cr,cc)in visit:
                            continue
                        if grid[cr][cc]:
                            return res
                        queue.append([cr,cc])
                        visit.add((cr,cc))
                res+=1
        for r in range(length):
            for c in range(length):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()