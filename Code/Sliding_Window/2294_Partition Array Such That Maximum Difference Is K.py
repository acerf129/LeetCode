class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        req=1
        minv=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-minv>k:
                minv=nums[i]
                req+=1
        return req