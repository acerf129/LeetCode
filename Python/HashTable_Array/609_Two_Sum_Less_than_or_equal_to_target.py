# Given an array of integers, find how many pairs in the array such that their sum is

# less than or equal toa specific target number. Please return the number of pairs.
# sort nums first +... <=target res+= i-firstindex+1
class Solution:
    target=24
    nums=[2, 7, 11, 15]
    def getCount(nums:list[int])->int:
        if len(nums)<2:
            return 0
        target=24
        nums.sort()
        n=len(nums)
        l=0
        r=n-1   
        req=0
        while l<r:
            while nums[l]+nums[r]>target and r>l:
                r-=1
            print(l,r)
            req+=r-l
            l+=1
        return req
    print(getCount(nums))