class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(i,val):
            if i==len(s):
                return True
            
            for j in range(i,len(s)):                
                sval=int(s[i:j+1])
                if sval+1==val and dfs(j+1,sval):
                    return True
            return False
            
            
        for i in range(len(s)-1):
            val=int(s[:i+1])            
            if dfs(i+1,val):
                return True
        return False