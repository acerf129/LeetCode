class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        req=0
        cur=0
        for cost,cash in transactions:
            req+=max(0,cost-cash)
            cur=max(cur,min(cost,cash))
        return req+cur
    