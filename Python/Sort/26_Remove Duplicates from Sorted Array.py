class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        n=len(nums)
        for r in range(l,n):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l