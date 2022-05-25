class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #2 d dynamic projramming
        #O(n)space complexity
        dp=[0]*(amount+1)
        dp[0]=1
        for c in coins:
            for i in range(1,amount+1):
                if i-c>=0:
                    dp[i]+=dp[i-c]
        return dp[-1] 
    #amount
    #  5 4  3  2  1 0
    #1 4  3  2  2  1  1
    #2 1  1  0  1  0  1
    #5 1  0  0  0  0  1
    #

        #Backtracking
        #O(n*M)
        cache={}
        def dfs(i,cur):
            if cur<0 or i==len(coins):
                return 0
            if cur==0: return 1 
            if (i,cur) in cache:
                return cache[(i,cur)]
                  
            cache[(i,cur)]=dfs(i,cur-coins[i])+dfs(i+1,cur)
            return cache[(i,cur)]
        return dfs(0,amount)
        #DP
        dp=[[0]*(len(coins)+1) for i in range(amount+1)]
        dp[0]=[1]*(len(coins)+1)
        #row for a col for c
        for a in range(1,amount+1):
            for c in range(len(coins)-1,-1,-1):
                dp[a][c]=dp[a][c+1]
                if a-coins[c]>=0:
                    dp[a][c]+=dp[a-coins[c]][c]
        return dp[amount][0]