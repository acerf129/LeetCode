class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        req=max(nums)
        cur1=0
        cur2=0
        for n in nums:            
            if cur1<0:
                cur1=0
            if cur2>0:
                cur2=0
            cur1+=n
            cur2+=n
            req=max(req,abs(cur1),abs(cur2))
        return req