class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        req=0
        #True True =False ,False False =False
        for n in nums:
            req=req^n
        return req