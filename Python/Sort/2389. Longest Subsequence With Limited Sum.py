class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix=list(accumulate(nums))
        req=[0]*len(queries)
        for i,q in enumerate(queries):
            l,r=0,len(prefix)-1
            while l<=r:
                mid=(l+r)//2
                if prefix[mid]<=q:
                    req[i]=mid+1
                    l=mid+1
                else:                    
                    r=mid-1
        return req
                    