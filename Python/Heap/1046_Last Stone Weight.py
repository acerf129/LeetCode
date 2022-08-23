class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-n for n in stones ]
        heapq.heapify(heap)
        while len(heap)>=2:
            first=heapq.heappop(heap)
            second=heapq.heappop(heap)
            val=first-second
            heapq.heappush(heap,val)
        return(-heap[0])