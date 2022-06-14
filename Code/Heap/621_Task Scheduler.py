class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #O(n*m)
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]            
        heapq.heapify(maxHeap)
        
        time=0
        queue=deque()#pair of [-cnt,idleTime]
        while queue or maxHeap:
            time+=1#each iteration
            
            if maxHeap:
                pops=1+heapq.heappop(maxHeap)
                if pops:
                    queue.append([pops,time+n])
            if queue and queue[0][1]==time:
                value,time= queue.popleft()
                heapq.heappush(maxHeap,value)
        return time