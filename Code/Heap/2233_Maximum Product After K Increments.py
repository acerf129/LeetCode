class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        minHeap=[]
        dic={}
        req=1
        for n in nums:
            dic[n]=dic.get(n,0)+1
        for v,c in dic.items():
            heapq.heappush(minHeap,[v,c])
        
        while k:
            val,count=heapq.heappop(minHeap)
            minv=min(k,count)
            if count-minv>0:
                heapq.heappush(minHeap,[val,count-minv])
            if minHeap and  minHeap[0][0]==val+1:
                minHeap[0][1]+=minv
            else:
                heapq.heappush(minHeap,[val+1,minv])
            k-=minv
        while minHeap:
            val,count=heapq.heappop(minHeap)
            req*=(val**count)
            req%=(10**9+7)
        return req%(10**9+7)