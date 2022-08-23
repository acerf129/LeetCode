class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            index=(l+r)//2
            mid=nums[index]
            if mid==target:
                return index                
            if mid<target:
                l=index+1
            else:
                r=index-1
        return -1