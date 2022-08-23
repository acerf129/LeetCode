class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False
        dp=set()
        dp.add(0)
        target=total//2
        for i in range(len(nums)-1,-1,-1):
            nextdp=set()
            for t in dp:
                if t+nums[i] ==target:
                    return True
                nextdp.add(t)
                nextdp.add(t+nums[i])
            dp=nextdp
        return  target in dp 
    #O(sum(n))