class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[0]
        for weight in w:
            self.prefix.append(weight+self.prefix[-1])
    def pickIndex(self) -> int:
        rand=random.randint(1,self.prefix[-1])
        index=bisect.bisect_left(self.prefix,rand)        
        return index-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()