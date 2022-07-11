class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        count=1
        for i in range(1,n+1):
            if count*2==i:
                count=i
            dp[i]=1+dp[i-count]                
        return dp
            