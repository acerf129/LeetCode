class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lens1=len(word1)
        lens2=len(word2)
        dp=[[float('inf')]*(lens2+1) for i in range(lens1+1)]
        for i in range(lens1+1):
            dp[i][-1]=lens1-i
            
        for j in range(lens2+1):
            dp[-1][j]=lens2-j
            
        for i in range(lens1-1,-1,-1):
            for j in range(lens2-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]