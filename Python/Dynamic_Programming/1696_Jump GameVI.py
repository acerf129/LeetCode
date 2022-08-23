
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        def dp(i):
            if i==0:
                return nums[0]
            return nums[i]+max(dp(j)for j in range(max(0,i-k),i))
        return dp(k)
        #Monotonic Queue: store unique value of
        #dp[i-k+1~i]in descending order
        n=len(nums)
        q=deque([0])#insert index
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            #q is descending
            dp[i]=nums[i]+dp[q[0]]
            #when dp[i]>= newest pop it
            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            #when index>q[0](oldest value)
            while q and i-q[0]>=k:
                q.popleft()
            q.append(i)
            print(q)
        return dp[-1] 