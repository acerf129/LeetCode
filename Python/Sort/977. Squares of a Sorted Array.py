class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        req=[]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]**2<nums[r]**2:
                req.append(nums[r]**2)
                r-=1
            else:
                req.append(nums[l]**2)
                l+=1
        req.reverse()
        return req