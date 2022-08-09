class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur=1        
        l=0
        req=0        
        for r in range(len(nums)):
            cur*=nums[r]
            while cur>=k and l<len(nums):
                cur/=nums[l]
                l+=1
            req+=(r-l+1)
        return req if req>0 else 0