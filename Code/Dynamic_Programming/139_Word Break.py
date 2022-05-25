class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={}
        def dfs(i):
            if i==len(s):
                return True
            if i in cache:
                return cache[(i)]
            cache[(i)]=False
            for c in wordDict:
                lens=len(c)
                if c==s[i:i+lens]:            
                    i+=lens
                    cache[(i)]= (dfs(i) or cache[(i)])
                    if cache[(i)]:
                        break
                    i-=lens                
            return cache[(i)]
        return dfs(0)
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]==True:
                    break
        return dp[0]