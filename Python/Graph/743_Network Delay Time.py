class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pMap=defaultdict(list)
        time=0
        visit=set()
        minHeap=[]
        for f,t,d in times:
            pMap[f].append([d,t])
        minHeap.append([0,k])#dist node
        while minHeap:
            dist1,node1=heapq.heappop(minHeap)
            if node1 in visit:
                continue
            visit.add(node1)
            time=max(time,dist1)
            for dist2,node2 in pMap[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap,[dist1+dist2,node2])
        
        return time if len(visit)==n else -1