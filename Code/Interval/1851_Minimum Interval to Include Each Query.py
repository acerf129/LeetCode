class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        req,minHeap={},[]
        i=0
        for q in sorted(queries):
            while i<len(intervals)and q>=intervals[i][0]:
                l,r=intervals[i]
                heapq.heappush(minHeap,(r-l+1,r))
                i+=1
            while minHeap and minHeap[0][1]<q:
                heapq.heappop(minHeap)
            req[q]=minHeap[0][0] if minHeap else -1
            
        return [req[q] for q in queries]