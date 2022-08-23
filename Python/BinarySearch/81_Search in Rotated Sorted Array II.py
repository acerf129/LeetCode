class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            #in left side
            if nums[mid]==nums[l]:
                l+=1
                continue
            if nums[mid]>=nums[l]:
                #go right
                if target<nums[l] or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                #go left
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return False