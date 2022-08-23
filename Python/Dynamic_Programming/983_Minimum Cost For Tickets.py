class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #decicion tree
        #dp means min of the cost of days
        #dp[i]=dp[i+d]+cost
        dp={}
        total=0        
        def dfs(i):
            if i==len(days):
                return 0
            if (i)in dp:
                return dp[(i)]
            dp[i]=float('inf')
            for d,c in zip([1,7,30],costs):
                j=0
                #days 7 <dats 8
                while j<len(days) and days[j]<days[i]+d:
                    j+=1
                dp[i]=min(dp[i],c+dfs(j))
            return dp[i]
        return dfs(0)