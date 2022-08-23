class Solution:
    def JumpGameVI(self, nums: List[int], k: int) -> int:
        #Monotonic QUEUE
        q=deque([0])#index
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=nums[i]+dp[q[0]]
            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            while q and i-k>=q[0]:
                q.popleft()
            q.append(i)
        return dp[-1]
            