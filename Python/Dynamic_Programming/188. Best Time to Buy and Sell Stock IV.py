class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,j,check):
            if i>=n:
                return 0
            if j==0:
                return 0
            buy,sell=0,0
            if check:
                buy=max(dfs(i+1,j,not check)-prices[i],dfs(i+1,j,check))
            else:
                sell=max(dfs(i+1,j-1,not check)+prices[i],dfs(i+1,j,check))
            return max(buy,sell)
        
        return dfs(0,k,True)