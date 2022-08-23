class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*(n+1)
        dp[-1]=True
        for i in range(n-2,-1,-1):
            if nums[i]==nums[i+1]:
                if dp[i]:
                    continue
                dp[i]=True
                dp[i]=dp[i] and dp[i+2]
            if i+2<n and nums[i]==nums[i+2] and nums[i]==nums[i+1]:
                if dp[i]:
                    continue
                dp[i]=True
                dp[i]=dp[i] and dp[i+3]
            if i+2<n and nums[i]+1==nums[i+1] and nums[i]+2==nums[i+2]:
                if dp[i]:
                    continue
                dp[i]=True
                dp[i]=dp[i] and dp[i+3]      
        return dp[0]