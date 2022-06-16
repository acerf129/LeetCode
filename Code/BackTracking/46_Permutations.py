class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        req=[]

        def dfs(count,cur):
            if len(cur)==len(nums):
                req.append(cur.copy())
                return
            for c in count:
                if count[c]>0:
                    count[c]-=1
                    cur.append(c)
                    dfs(count,cur)
                    cur.pop()
                    count[c]+=1
            return 
        dfs(count,[])
        return req