class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix=list(accumulate(nums,initial=0))
        req=0
        temp=0
        l=0
        for i in range(1,len(prefix)):
            temp=(prefix[i]-prefix[l])*(i-l)
            while temp>=k:
                l+=1
                temp=(prefix[i]-prefix[l])*(i-l)
            req+=(i-l)
            
        return req