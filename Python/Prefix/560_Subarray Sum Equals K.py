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

        prefix=list(accumulate(nums,initial=0))
        cache={}
        req=0
        for i in range(len(prefix)):
            if prefix[i]-k in cache:
                req+=cache[prefix[i]-k]
            cache[prefix[i]]=cache.get(prefix[i],0)+1    
        return req