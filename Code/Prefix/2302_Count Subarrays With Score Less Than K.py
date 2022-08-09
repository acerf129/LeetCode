class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix=list(accumulate(nums,initial=0))
        req=0
        l=0
        for r in range(1,len(prefix)):
            temp=(r-l)*(prefix[r]-prefix[l])
            while temp>=k:                
                l+=1
                temp=(r-l)*(prefix[r]-prefix[l])
            req+=(r-l)
        return req