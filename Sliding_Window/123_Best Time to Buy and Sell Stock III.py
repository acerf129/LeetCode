class Solution:       
    def maxProfit(self, prices: List[int]) -> int:
        #DP
        buy=[-prices[0]]*2
        sell=[0]*2
        for i in range(1,len(prices)):
            buy[0]=max(buy[0],-prices[i])
            sell[0]=max(sell[0],prices[i]+buy[0])
            buy[1]=max(buy[1],sell[0]-prices[i])
            sell[1]=max(sell[1],prices[i]+buy[1])
        return sell[1]

        #Memorization
        dp={}        
        def dfs(i,t,buy):
            if i==len(prices) or t==0:
                return 0 
            if (i,t,buy) in dp:
                return dp[(i,t,buy)]        
            #buy
            if buy:            
                buys=dfs(i+1,t,0)-prices[i]
                cool=dfs(i+1,t,1)
                dp[(i,t,buy)]=max(buys,cool)
            #sell
            else:                    
                sell=dfs(i+1,t-1,1)+prices[i]
                cool=dfs(i+1,t,0)
                dp[(i,t,buy)]=max(sell,cool)
            return dp[(i,t,buy)]    
        return dfs(0,2,1)
