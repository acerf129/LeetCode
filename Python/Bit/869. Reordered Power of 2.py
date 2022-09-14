class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count=Counter(str(n))
        
        return any(count==Counter(str(1<<i)) for i in range(31))
