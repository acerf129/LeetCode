class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(len(nums)):
            total+=nums[i]-nums[0]
        return total