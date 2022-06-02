class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        req=0
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            #check leftside
            if nums[mid]>=nums[l]:
                #go right or  right side
                if target>nums[mid] or nums[l]>target:
                    l=mid+1
                else:
                    r=mid-1
            #right side
            else:
                #go left or leftside
                if nums[r]<target or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
                