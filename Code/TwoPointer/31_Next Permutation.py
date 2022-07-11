class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)-2,-1,-1):
            if nums[j]<nums[j+1] :
                i=j
                break
        if i>=0:
            k=len(nums)-1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    k=j
            nums[i],nums[k]=nums[k],nums[i]
        l,r=i+1 ,len(nums)-1
        while l<r:
            if nums[l]>nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            else:
                r-=1