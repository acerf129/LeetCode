class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        check=[]
        for i in range(len(nums)):
            if nums[i]==key:
                check.append(i)
        l=0 #2 5
        res=[]
        for i in range(len(nums)):
            if l<len(check)and  i-check[l]>k:
                l+=1
            if l<len(check)and  abs(i-check[l])<=k:
                res.append(i)
        return res