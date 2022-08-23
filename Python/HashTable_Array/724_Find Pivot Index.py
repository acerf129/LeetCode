class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums=sum(nums)
        cur=0
        for i in range(len(nums)):            
            if sums-nums[i]-cur==cur:
                return i
            cur+=nums[i]
        return -1