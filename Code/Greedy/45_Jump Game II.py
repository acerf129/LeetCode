class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        req=0
        #window update for l to right get the farest
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far= max(far,i+nums[i])
            l,r=r+1,far
            req+=1
        return req

        dp=[float('inf') for i in range(len(nums))]
        dp[0]=0
        #dp i =
        for i in range(len(nums)):
            r=i+nums[i]
            for j in range(i,min(len(nums),r+1)):                
                dp[j]=min(dp[j],1+dp[i])
        return dp[-1]