class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dic={}
        req=[]
        for n in nums:
            dic[n]=dic.get(n,0)+1
            
        for k,v in dic.items():
            if v==1 and k-1 not in dic and k+1 not in dic:
                req.append(k)
        return req