class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        req=[]
        lens=len(nums)
        for n in nums:
            dic[n]=dic.get(n,0)+1
            if n in req:
                continue
            if dic[n]>lens/3:
                req.append(n)       
        return req