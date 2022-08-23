class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        pMap={i:[] for i in range(n)}
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                pMap[i].append([dist,j])
                pMap[j].append([dist,i])
        req=0
        visit=set()
        minHeap=[[0,0]]#cost,point
        while len(visit)<n:
            cost,i=heapq.heappop(minHeap)
            if i in visit:
                continue
            req+=cost
            visit.add(i)
            for dist,j in pMap[i]:
                if j not in visit:
                    heapq.heappush(minHeap,[dist,j])
        return req