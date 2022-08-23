class Solution:
    def minDays(self, n: int) -> int:
        #return the minimum number of days 
        #dp[i]=1+dp[i-j]
        dp={0:0,1:1,2:2}
        def dfs(i):
            if i in dp:
                return dp[i]
            one =1+(i%2)+dfs(i//2)
            
            #12 - 8=4 
            two = 1+(i%3)+dfs(i//3)
            dp[i]=min(one,two)
            return dp[i]
        return dfs(n)