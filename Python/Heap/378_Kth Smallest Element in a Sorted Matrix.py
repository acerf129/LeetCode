class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row=len(matrix)
        maxHeap=[]
        for i in range((row)):
            for j in range((row)):
                heapq.heappush(maxHeap,-matrix[i][j])
                if len(maxHeap)>k:
                    heapq.heappop(maxHeap)
        return -maxHeap[0]