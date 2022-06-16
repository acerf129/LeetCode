class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        req=[]
        nums.sort()
        def dfs(i,cur):
            if i==len(nums):
                req.append(cur.copy())
                return 
            # include nums[i]
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            
            #not include nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,cur)            
            return 
        dfs(0,[])
        return req