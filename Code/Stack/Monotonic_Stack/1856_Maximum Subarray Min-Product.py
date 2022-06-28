class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack=[]#start val
        req=0
        prefix=[0]
        for n in nums:
            prefix.append(prefix[-1]+n)
        
        for i,n in enumerate(nums):
            start=i
            while stack and stack[-1][1]>n:
                index,val=stack.pop()
                start=index
                req=max(req,(prefix[i]-prefix[index])*val)   
            stack.append([start,n])
            
        for i,v in stack:
            val=(prefix[len(nums)]-prefix[i]) * v
            req=max(req,val)    
        
        return req%(10**9+7)