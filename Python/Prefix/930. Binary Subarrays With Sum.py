class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        prefix=list(accumulate(nums,initial=0))
        dic={}
        req=0
        #prefix[j]-prefix[i]=goal 4-2=2
        for n in prefix:
            req+=dic.get(n,0)
            dic[n+goal]=dic.get(n+goal,0)+1

        return req