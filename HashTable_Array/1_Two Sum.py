class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dic index value value
        dic={}
        for i in range(len(nums)):     
            if dic and target-nums[i] in dic:
                return[i,dic[target-nums[i]]]
            if nums[i]not in dic:
                dic[nums[i]]=i
            