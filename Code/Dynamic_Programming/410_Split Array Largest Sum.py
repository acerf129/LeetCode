class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp={}
        
        def dfs(i,g):
            if i==len(nums)or g<=0:
                return 0
            if g==1:
                return sum(nums[i:])
            if (i,g)in dp:
                return dp[(i,g)]
            res,curSum=float('inf'),0
            for j in range(i,len(nums)-g+1):
                curSum+=nums[j]
                maxSum=max(curSum,dfs(j+1,g-1))
                res=min(res,maxSum)
                if curSum>res:
                    break
            dp[(i,g)]=res
            return dp[(i,g)]
        return dfs(0,m)