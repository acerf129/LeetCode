def subarray_sum_equals_k_i_i(self, nums, k):
        # write your code here
        if k in nums:
            return 1
        req=float('inf')
        prefix=[]
        dic={}
        for i in range(len(nums)):
            if not prefix:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]+prefix[-1])
            last=prefix[-1]
            if last not in dic:
                dic[last]=[]
            dic[last].append(i)
            if last==k:
                req=min(req,i+1)
            if last-k in dic:
                req=min(req,i-dic[last-k][-1])

        return req if req !=float('inf') else -1