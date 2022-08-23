class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        
        for i in range(1,target+1):
            dp[i]=0
            for j in range(len(nums)):
                if i-nums[j]>=0:
                    dp[i]+=dp.get(i-nums[j],0)
        return dp[target]
    def combinationSum4(self, nums: List[int], target: int) -> int:        
        dp=[0]*(target+1)
        dp[0]=1
        #dp[i]=        
        for tar in range(1,target+1):
            for c in nums:
                if tar-c>=0:
                    dp[tar]+=dp[tar-c]
        return dp[-1]