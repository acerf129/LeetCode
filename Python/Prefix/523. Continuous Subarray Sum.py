class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix=list(accumulate(nums,initial=0))
        cache={}
        for i in range(len(prefix)):            
            if prefix[i]%k in cache and  i-cache[prefix[i]%k]>=2:
                return True
            if prefix[i]%k not in cache:
                cache[prefix[i]%k]=i
        return False