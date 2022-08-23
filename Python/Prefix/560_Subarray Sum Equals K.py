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

        prefix=[]
        dic={}
        req=0
        for n in nums:
            if not prefix:
                prefix.append(n)
            else:
                prefix.append(n+prefix[-1])
            dic[prefix[-1]]=dic.get(prefix[-1],0)+1
            if prefix[-1]==k :
                req+=1
            if  prefix[-1]-k in dic:
                req+=dic[prefix[-1]-k]
        return req