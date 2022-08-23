class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        check=set()
        cur,req,l=0,0,0
        for n in nums:
            while n in check:
                cur-=nums[l]
                check.remove(nums[l])
                l+=1
            check.add(n)
            cur+=n
            req=max(req,cur)
        return req