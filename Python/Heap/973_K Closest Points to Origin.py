class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            val=x**2+y**2
            minHeap.append([val,x,y])
        heapq.heapify(minHeap)
        req=[]
        while k:
            pops=heapq.heappop(minHeap)
            k-=1
            req.append([pops[1],pops[2]])
        return req