class Solution:
    def jump(self, nums: List[int]) -> int:
        req=0
        l,r=0,0
        while r<len(nums):
            far=0
            for i in range(l,r+1):
                far=max(far,nums[l]+i)
            l=r+1
            r=far
            req+=1
        return req
        #min step
        #0 1 1 2 2
        #num[j] = min(num[i]+1)
        req=[0]*(len(nums))
        if len(nums)==1:
            return 0
        for i in range(0,len(nums)):            
            farest=i+nums[i]
            
            #check the minimun of the jump
            for j in range(i+1,farest+1):                
                if j<len(nums):                        
                    if req[j]==0: req[j]=req[i]+1
                    else: req[j]=min(req[j],req[i]+1)
        return req[-1]