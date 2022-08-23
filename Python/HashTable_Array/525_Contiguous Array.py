class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        req=0
        sums=0
        dic={}#sums,index
        #[1,0,1,1,0,0,1]
    #sums 1 0 1 2 1 0 1
    #     index 2 -index 0 
        for i,n in enumerate(nums):
            if n==1:
                sums+=1
            else:
                sums-=1
            if sums in dic:
                req=max(req,i-dic[sums])
            else:
                dic[sums]=i
            if sums==0:
                req=max(req,i+1)
        return req