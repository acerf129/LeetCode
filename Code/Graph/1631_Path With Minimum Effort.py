class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights),len(heights[0])
        req=0
        minHeap=[[0,0,0]]#dis,r,c
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while minHeap:
            dis,r,c=heapq.heappop(minHeap)
            visit.add((r,c))
            req=max(req,dis)
            if r==rows-1 and c==cols-1:
                return req
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr,nc)in visit or nr<0 or nc<0 or nr==rows or nc==cols:
                    continue
                val=abs(heights[nr][nc]-heights[r][c])
                heapq.heappush(minHeap,[val,nr,nc])