class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        req=[]
        cur=[]
        def backtrack(i,count):
            if len(cur)==len(nums):
                req.append(cur.copy())                
                return
            for c in count:
                if count[c]>0:
                    count[c]-=1
                    cur.append(c)
                    backtrack(i+1,count)
                    cur.pop()
                    count[c]+=1
            return
        backtrack(0,count)
        
        return req