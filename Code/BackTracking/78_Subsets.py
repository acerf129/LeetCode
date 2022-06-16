class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        req=[]
        
        def dfs(i,cur):
            if i>=len(nums):
                req.append(cur.copy())
                return
            
            one=dfs(i+1,cur)
            two=dfs(i+1,cur+[nums[i]])
            return
        dfs(0,[])
        
        return req