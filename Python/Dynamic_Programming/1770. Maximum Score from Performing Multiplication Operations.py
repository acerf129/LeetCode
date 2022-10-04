class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m,n=len(multipliers),len(nums)
        dp=[0]*(m+1)
        
        for i in range(m-1,-1,-1):
            temp=dp.copy()
            for j in range(i,-1,-1):
                dp[j]=max(nums[j]*multipliers[i]+temp[j+1],nums[n-1-(i-j)]*multipliers[i]+temp[j])
        return dp[0]