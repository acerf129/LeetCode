class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        req=0
        minHeap=[]
        minHeap.append([grid[0][0],0,0])
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while minHeap:
            dist,r,c=heapq.heappop(minHeap)
            visit.add((r,c))
            req=max(req,dist)
            if r==rows-1 and c==cols-1:
                break
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if (nr,nc) in visit or nr<0 or nc<0 or nr==rows or nc==cols:
                    continue
                heapq.heappush(minHeap,[grid[nr][nc],nr,nc])
        return req