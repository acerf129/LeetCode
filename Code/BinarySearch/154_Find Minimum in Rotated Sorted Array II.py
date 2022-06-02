class Solution:
    def findMin(self, nums: List[int]) -> int:
       if nums[-1]>nums[0]:
            return nums[0]

       l,r=0,len(nums)-1
       req=float('inf')
       while l<=r:
            mid=(l+r)//2
            #on the left side
            req=min(req,nums[mid])
            if nums[mid]==nums[r]:
                r-=1
            elif nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
       return req