class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        gascount=0
        req=0
        for i in range(len(gas)):
            gascount+=gas[i]-cost[i]
            if gascount<0:
                gascount=0
                req=i+1
        return req