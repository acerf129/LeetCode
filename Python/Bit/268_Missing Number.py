class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        req=0
        for i in range(len(nums)+1):
            if i<len(nums):
                req=req^nums[i]            
            req=req^i
        return req