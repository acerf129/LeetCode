class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        req=max(nums)
        cmin=1
        cmax=1
        for n in nums:
            if n==0:
                cmin,cmax=1,1
                continue
            temp=cmax
            cmax=max(cmax*n,cmin*n,n)
            cmin=min(temp*n,cmin*n,n)
            req=max(req,cmax )
        return req