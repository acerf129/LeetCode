class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #backtrack
        visit=set()#index
        def dfs(i):
            if i>=len(arr) or i<0:
                return False
            if arr[i]==0:
                return True
            if i in visit:
                return False
            
            req=False
            visit.add(i)
            req= dfs(i+arr[i]) or dfs(i-arr[i]) 
            visit.remove(i)
            return req
        return dfs(start)