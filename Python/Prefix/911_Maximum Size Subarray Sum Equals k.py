def max_sub_array_len(self, nums, k):
        # Write your code here
        dic={}
        prefix=[]
        req=0
        for i,v in enumerate(nums):
            
            if not prefix:
                prefix.append(v)
            else:
                prefix.append(v+prefix[-1])
            if prefix[-1] not in dic:
                dic[prefix[-1]]=[]
            dic[prefix[-1]].append(i)
            if prefix[-1]==k:
                req=max(req,i+1)
            if prefix[-1]-k in dic:
                val=i-dic[prefix[-1]-k][0]
                req=max(req,val)
        return req