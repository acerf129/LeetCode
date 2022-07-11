class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1]and nums[i]>nums[i+1]:
                return i
        req=0
        for j in range(len(nums)):
            if nums[j]>nums[req]:
                req=j
        return req