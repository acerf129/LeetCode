class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif mid-1>=0 and  nums[mid]>target>nums[mid-1]:
                return mid
            elif mid+1<len(nums) and nums[mid+1]>target>nums[mid]:
                return mid+1
            elif target>nums[mid]:
                l=mid+1               
            else:
                r=mid-1