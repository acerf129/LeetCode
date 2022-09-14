class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        cur=l=0
        n=len(chargeTimes)
        queue=deque()
        for r in range(n):
            #get max value
            cur+=runningCosts[r]
            while queue and chargeTimes[queue[-1]]<=chargeTimes[r]:
                queue.pop()
            queue.append(r)
            if  queue and  chargeTimes[queue[0]]+(r-l+1)*cur>budget:
                cur-=runningCosts[l]
                if queue[0]==l:
                    queue.popleft()
                l+=1
        
        return n-l