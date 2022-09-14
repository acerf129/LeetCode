class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #start from 0 two pointer
        l=0
        n=len(nums)
        for r in range(n):
            if nums[r]!=val:
                nums[l]=nums[r]
                l+=1
        
        return l