class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for n in nums:
            if n-1 not in numset:
                long=0
                while n+long in numset:
                    long+=1
                longest=max(longest,long)
        return longest

        check=set(nums)
        req=0
        cur=0
        count=0
        for n in check:
            if n-1 not in check:
                cur=n
                count=1
            while cur+1 in check:
                cur+=1
                count+=1
            req=max(req,count)
        return req