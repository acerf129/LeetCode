class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        minHeap=[]
        second=0
        queue=[]
        req=[]
        for i,s in enumerate(servers):
            heapq.heappush(minHeap,[s,i])
        for i in range(len(tasks)):
            second=max(second,i)
            if not minHeap:
                second=queue[0][0]
            while queue and queue[0][0]<=second:
                s,v,index=heapq.heappop(queue)
                heapq.heappush(minHeap,[v,index])
                
            val,index=heapq.heappop(minHeap)
            heapq.heappush(queue,[second+tasks[i],val,index])
            req.append(index)               
        return req