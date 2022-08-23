class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        minHeap=[[0,0,0]]#d,r,c
        distance=[[float('inf')]*cols for i in range(rows)]
        while minHeap:
            d,r,c=heapq.heappop(minHeap)
            if d>distance[r][c]:
                continue
            if (r,c)==(rows-1,cols-1):
                return d
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc=r+dr,c+dc
                if rows>nr>=0 and cols>nc>=0:
                    nd=d
                    if grid[nr][nc]==1:
                        nd+=1
                    if nd<distance[nr][nc]:
                        distance[nr][nc]=nd                        
                        heapq.heappush(minHeap,[nd,nr,nc])
            