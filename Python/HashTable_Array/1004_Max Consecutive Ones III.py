class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,req,count=0,0,0
        n=len(nums)
        #1 1 1 0 0 =5  ,k=2
        for j in range(n):
            if nums[j]==0:
                count+=1
            while count>k:
                if nums[i]==0:
                    count-=1
                i+=1
            req=max(req,j-i+1)
            print(req)
        return req