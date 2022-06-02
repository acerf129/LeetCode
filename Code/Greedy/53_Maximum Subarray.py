class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=0
        req=nums[0]
        for n in nums:            
            if curSum<0:
                curSum=0
            curSum+=n
            req=max(req,curSum)
        return req