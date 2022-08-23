class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,0
        req=0
        for p  in range(len(prices)):
            if prices[p]<=prices[l]:
                l=p
            if p>l and prices[p]>prices[l]:
                r=p                
                req=max(req,prices[r]-prices[l])
        return(req)