class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #get maximum of the dp[0]123
        #set the last pop value left right 
        lens=len(nums)
        if lens==0:
            return 0
        dp=[[0]*lens for _ in range(lens)]
        
        for l in range(lens-1,-1,-1):
            for r in range(l,lens):
                for i in range(l,r+1):
                    left=1 if l==0 else nums[l-1]
                    right=1 if r==lens-1 else nums[r+1]
                    
                    lpart=0 if l>i-1 else dp[l][i-1]
                    rpart=0 if r<i+1 else dp[i+1][r]
                    
                    cur=nums[i]*left*right
                    prev=lpart+rpart
                    dp[l][r]=max(dp[l][r],cur+prev)
                    
        return dp[0][-1]
        nums=[1]+nums+[1]
        dp={}
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        def dfs(l,r):
            if l>r:
                return 0
            if (l,r)in dp:
                return dp[(l,r)]
            dp[(l,r)]=0
            #if i is the last pop
            for i in range(l+1,r):
                coins=nums[l]*nums[i]*nums[r]
                coins+=dfs(l,i)+dfs(i,r)
                dp[(l,r)]=max(dp[(l,r)],coins)
            return dp[(l,r)]
        return dfs(0,len(nums)-1)