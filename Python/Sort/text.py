# /*
# Given a sorted array *nums*, remove the duplicates in-place such that each element appears only *once* and returns the new length.

# Do not allocate extra space for another array, you must do this by **modifying the input array in-place with O(1) extra memory.

# Note
# - You cannot change the size of the input array
# - return value is a number. And the array is simply modified in-place. Only the first N numbers are un-duplicated, and the rest of the array does not matter.

# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Return. value: 5
# The input array is changed to = [0,1,2,3,4,...] (it doens't matter what numbers are after the first 5)
# */           
                                  
# [0, 0, 1, 1, 2] -> [0, 1, 1, 2, 0]
#[1,2,0,1,0]                                      
#res+=1 if cur !=n in nums
def getlen(nums):
   n=len(nums)
   if n<=1:
      return n
   l=1
   for r in range(1,n):
      if nums[r]!=nums[r-1]:
         nums[l]=nums[r]
         l+=1
   print(nums)
   return l
nums = [0,1,1,1,1,2,2,3,3,4]
print(getlen(nums))