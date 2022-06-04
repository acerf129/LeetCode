class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]
        l,r=0,len(nums)-1
        req=[]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        
        if l<len(nums) and  nums[l]==target:
            req.append(l)
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<=target:
                l=mid+1         
            else:
                r=mid-1        
        if r>=0 and  nums[r]==target:
            req.append(r)
        return req if req!=[] else [-1,-1]