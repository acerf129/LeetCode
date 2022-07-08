class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap=[]
        stack=[]
        if a:
            heapq.heappush(maxHeap,[-a,"a"])
        if b:
            heapq.heappush(maxHeap,[-b,"b"])
        if c:
            heapq.heappush(maxHeap,[-c,"c"])
        
        while maxHeap :
            count,val=heapq.heappop(maxHeap)
            if len(stack)<2 or (len(stack)>=2 and stack[-1]!=val or stack[-2]!=val) :
                stack.append(val)
                if count+1!=0:
                    heapq.heappush(maxHeap,[count+1,val])
            else:
                if not maxHeap:
                    break
                count2,val2=heapq.heappop(maxHeap)
                stack.append(val2)
                heapq.heappush(maxHeap,[count,val])
                if count2+1!=0:
                    heapq.heappush(maxHeap,[count2+1,val2])
        return "".join(stack)