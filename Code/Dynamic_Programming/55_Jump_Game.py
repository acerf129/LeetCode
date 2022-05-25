class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #DP
        #bottom up 
        #index = i +num[i]
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal==0