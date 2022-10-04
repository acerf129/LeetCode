class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod=10**9+7
        pair =[[e,s] for e,s in  zip(efficiency,speed)]
        req=0
        cur=0
        heap=[]
        for e,s in sorted(pair)[::-1]:
            heapq.heappush(heap,s)
            cur+=s
            if len(heap)>k:
                cur-=heapq.heappop(heap)
            req=max(req,cur*e)
            
        return req%mod