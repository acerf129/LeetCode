class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        squares=[i**2 for i in range(0,n)if i**2 <=n]
        for i in range(1,n+1):
            for sq in squares:
                if i <sq:
                    break
                dp[i]=min(dp[i],1+dp[i-sq])
        return dp[-1]