def max_sub_array_len(self, nums, k):
        # Write your code here
        prefix=list(accumulate(nums,initial=0))
        req=0
        cache={}
        for i in range(len(prefix)):
            if prefix[i] not in cache:
                cache[prefix[i]]=i
            if prefix[i]-k in cache:
                req=max(req,i-cache[prefix[i]-k])
        return req