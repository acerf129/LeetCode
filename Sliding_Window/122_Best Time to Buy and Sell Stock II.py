class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        req=0
        
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                req+=prices[i]-prices[i-1]
        return req