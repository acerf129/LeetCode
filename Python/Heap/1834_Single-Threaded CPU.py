class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,v in enumerate(tasks):
            v.append(i)        
        tasks.sort(key=lambda x:(x[0],x[1]))
        res,minHeap=[],[]
        i,time=0,tasks[0][0]
        
        while minHeap or i<len(tasks):
                while i<len(tasks) and time>=tasks[i][0]:
                    heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                    i+=1
                if not minHeap:
                    if i<len(tasks):
                        time=tasks[i][0]
                else:
                    prosTime,index=heapq.heappop(minHeap)
                    time+=prosTime
                    res.append(index)
        return res