class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        req=[]        
        def backtrack(i,cur):
            if i==len(nums):
                res="".join(cur)
                return None if res in nums else res
            
            res=backtrack(i+1,cur)
            if res:
                return res
            cur[i]="1"
            res=backtrack(i+1,cur)
            if res:
                return res
        return backtrack(0,["0" for i in nums])
            