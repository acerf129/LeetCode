class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        req=0
        first=0
        second=sum(nums)
        for n in range(len(nums)-1):
            first+=nums[n]
            second-=nums[n]            
            if first>=second:
                req+=1
        return req