class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: List[int]):
        # write your code here
        
        for i in range(1,len(nums)):
            j=i-1
            if i%2:
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
            else:
                if nums[i]>nums[j]:
                    nums[j],nums[i]=nums[i],nums[j]