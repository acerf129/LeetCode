class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}
        
        def dfs(i,j):
            
            if i==len(s) and j==len(p):
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)]=False
            matchs=(i<len(s) and j<len(p) and ( s[i]==p[j] or p[j]=="."))
            if matchs:
                cache[(i,j)]=dfs(i+1,j+1)
            if j+1<len(p) and p[j+1]=="*":
                cache[(i,j)]=(matchs and dfs(i+1,j)or (dfs(i,j+2)))
            return cache[(i,j)]
        return dfs(0,0)