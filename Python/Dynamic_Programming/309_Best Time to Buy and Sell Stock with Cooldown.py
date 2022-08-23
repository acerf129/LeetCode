class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        #buy increment +1
        #sell by2
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            
            dp[(i,buy)]=0
            if buy:        
                dp[(i,buy)]= max(-prices[i]+dfs(i+1,not buy),dfs(i+1,buy))
            else:
                dp[(i,buy)]=max(prices[i]+dfs(i+2,not buy),dfs(i+1,buy))
            return dp[(i,buy)]
        return dfs(0,True)