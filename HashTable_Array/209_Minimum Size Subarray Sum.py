class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        req=float('inf')
        sums=0
        l,r=0,0
        for n in nums:
            sums+=n
            r+=1
            while sums>=target:
                req=min(req,r-l)
                sums-=nums[l]
                l+=1
        return req if req!=float('inf') else 0