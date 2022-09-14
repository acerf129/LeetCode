class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or k<0 :
            return False
        check={}
        for i in range(len(nums)):
            m=nums[i]//(t+1)
            if m in check or (m+1 in check and abs(check[m+1]-nums[i])<=t)or (m-1 in check and abs(check[m-1]-nums[i])<=t)  :
                return True            
            check[m]=nums[i]
            if i>=k:
                del check[nums[i-k]//(t+1)]
        return False