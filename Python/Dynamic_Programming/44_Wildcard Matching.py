class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def removedup(p):
            num=[]
            for c in p:
                if num and num[-1]=="*" and c=="*":
                    continue
                num.append(c)
            
            return "".join(num)
        p=removedup(p)
        lens=len(s)
        lenp=len(p)
        @cache
        def dfs(i,j):
            if i==lens and j==lenp:
                return True
            elif i==lens and j<lenp and p[j]=="*":
                return dfs(i,j+1)
            elif i==lens or j==lenp:
                return False
            if s[i]==p[j] or p[j]=="?":
                return dfs(i+1,j+1)
            if p[j]=="*":
                return dfs(i+1,j) or dfs(i,j+1)        
            return False        
        return dfs(0,0)