class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use every element as k i,j=left right
        #sort the nums
        #if the value same l+=1
        #after append req l+=1(check the remain value with same i)
        #[-4, -1, -1, 0, 1, 2]
        nums.sort()
        i,j=0,len(nums)-1
        k=1
        req=[]
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if v+nums[l]+nums[r]<0:
                    l+=1
                elif v+nums[l]+nums[r]>0:
                    r-=1        
                else:
                    req.append([v,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return req