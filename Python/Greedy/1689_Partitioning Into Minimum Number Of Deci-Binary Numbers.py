class Solution:
    def minPartitions(self, n: str) -> int:
        count=0
        for num in n:
            count=max(count,int(num))
            
        return count