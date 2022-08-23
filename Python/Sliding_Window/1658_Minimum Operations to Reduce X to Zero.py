class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sums=sum(nums)
        if sums<x:
            return -1
        if sums==x:
            return len(nums)
        req=float('inf')
        index=0
        cur=0
        lens=len(nums)
        for i,n in enumerate(nums):
            cur+=n
            if cur==x:
                req=min(req,i+1)
            if cur>x:
                cur-=n
                index=i-1
                break
        for j in range(len(nums)-1,-1,-1):
            cur+=nums[j]
            while cur>x:
                if index==-1:
                    break
                cur-=nums[index]
                index-=1
            if cur==x:
                req=min(req,index+1+lens-j)
                if index==-1:
                    break
                cur-=nums[index]
                index-=1
        return req if req!=float('inf') else -1