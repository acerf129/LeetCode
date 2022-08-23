class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        req=[]
        
        def dfs(i,cur):
            if i>=len(candidates):
                return 
            if cur and sum(cur)==target:
                req.append(cur.copy())
                return
            if cur and sum(cur)>target:
                return
            
            one=dfs(i,cur+[candidates[i]])
            two=dfs(i+1,cur)
            return
        
        dfs(0,[])
        return req