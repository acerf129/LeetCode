class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        count=0
        for n in nums:
            if n==0:
                count+=1
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1