class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod=10**9+7
        prefix=list(accumulate(nums,initial=0))
        n=len(nums)
        stack=[]
        req=max(nums)
        for i in range(len(nums)):
            index=i
            while stack and stack[-1][1]>nums[i]:
                index,value=stack.pop()
                pvalue=(prefix[i]-prefix[index])*value
                req=max(req,pvalue)
            stack.append([index,nums[i]])
        while stack:
            index,value=stack.pop()
            pvalue=(prefix[-1]-prefix[index])*value
            req=max(req,pvalue)
        return req%mod