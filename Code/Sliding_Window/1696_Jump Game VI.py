class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:        
        #monotonic Queue deque with DP
        #decreasing deque
        #if the rightest too small pop
        #if  the leftest too old popleft
        #dp[i]=nums[i]+dp[q[0]](the largestnumber)
        n=len(nums)
        q=deque([0])#index
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=nums[i]+dp[q[0]]
            #compare the value pop the index
            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            #index Comparison
            while q and i-q[0]>=k:
                q.popleft()
            q.append(i)
        return dp[-1]