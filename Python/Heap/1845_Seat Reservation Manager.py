class SeatManager:

    def __init__(self, n: int):
        self.minHeap=[i+1 for i in range(n)]
        heapq.heapify(self.minHeap)
    def reserve(self) -> int:
        val=heapq.heappop(self.minHeap)
        return val
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minHeap,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)