class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        lens=len(stones)
        if (lens-1)% (k-1)!=0:
            return -1
        prefix=list(accumulate(stones,initial=0))
        
        dp=[[0]*lens for _ in range(lens)]
        #3 4 
        #2 1
        
        for l in range(k,lens+1):
            for i in range(lens-l+1):
                j=i+l-1
                if l>k:
                    dp[i][j]=min(dp[i][t]+dp[t+1][j] for t in range(i,j,k-1))
                if (l-1)%(k-1)==0:
                    dp[i][j]+=prefix[j+1]-prefix[i]
                
        return dp[0][-1]