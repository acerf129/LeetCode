class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        lens=len(nums)
        dp=[0]*lens
        req=[[] for _ in range(lens)]
        for i in range(len(nums)):
            total=[nums[i]]
            for j in range(i):
                if not nums[i]%nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        total=req[j]+[nums[i]]                        
            req[i]=total
            
        return max(req,key=len)