class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visit=set()
        queue=deque()
        queue.append([0,0,k,0])#r,c,k,v
        rows,cols=len(grid),len(grid[0])
        while queue:
            r,c,l,v=queue.popleft()
            if (r,c) ==(rows-1,cols-1):
                return v
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc=r+dr,c+dc
                if rows>nr>=0 and cols>nc>=0 :
                    if grid[nr][nc]:
                        if l and (nr,nc,l-1) not in visit:
                            visit.add((nr,nc,l-1))
                            queue.append([nr,nc,l-1,v+1])
                    else:
                        if (nr,nc,l) not in visit:
                            visit.add((nr,nc,l))
                            queue.append([nr,nc,l,v+1])
        return -1