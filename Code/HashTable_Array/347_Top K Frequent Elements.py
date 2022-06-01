class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        if  len(nums)==1:
            return nums
        if k>len(nums):
            return []
        for n in nums:
            dic[n]=dic.get(n,0)+1
        req=sorted(dic.items(), key=lambda a:a[1], reverse=True)
        ans=[]
        for i in req:
            if len(ans)<k:
                ans.append(i[0])
            else:
                break
        return ans