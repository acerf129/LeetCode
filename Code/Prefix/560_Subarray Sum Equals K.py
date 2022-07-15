class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur=0
        req=0
        prefixSum={0:1}
        for n in nums:
            cur+=n
            diff=cur-k
            req+= prefixSum.get(diff,0)
            prefixSum[cur]=prefixSum.get(cur,0)+1
        return req