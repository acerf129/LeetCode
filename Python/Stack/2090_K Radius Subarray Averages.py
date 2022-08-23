class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        if len(nums)<2*k+1  :
            return [-1]*len(nums)
        req=[-1]*k
        l=0
        i=k
        r=2*k
        avgs=sum(nums[:(2*k+1)])
        res=[]
        for i in range(r,len(nums)):
            if i==r:
                #print(avgs)
                res.append(avgs//(2*k+1))                
            else:                
                avgs=avgs+nums[i]-nums[l]
                #print(avgs)
                res.append(avgs//(2*k+1))
                l+=1
        return req+res+req