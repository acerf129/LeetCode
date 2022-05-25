class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        cache={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs(i,j,k):
            if k==len(s3) :
                return True
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            cache[(i,j,k)]=False
            if i<len(s1)and s1[i]==s3[k]:
                cache[(i,j,k)]=(dfs(i+1,j,k+1)or cache[(i,j,k)])
            if j<len(s2)and  s2[j]==s3[k]:
                cache[(i,j,k)]=(dfs(i,j+1,k+1)or cache[(i,j,k)])
            return cache[(i,j,k)]
        return dfs(0,0,0)

        #DP array backtracking 
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s2)+1)for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)]=True
        
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]