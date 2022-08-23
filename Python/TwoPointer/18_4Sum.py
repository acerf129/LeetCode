class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()        
        req,quad=[],[]
        def kSum(k,index,tar):
            if k!=2:
                #4 left 2 for l,r
                for i in range(index,len(nums)-k+1):
                    if i>index and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1,i+1,tar-nums[i])
                    quad.pop()
            else:
                l,r=index,len(nums)-1
                while l<r:
                    if nums[l]+nums[r]<tar:
                        l+=1
                    elif nums[l]+nums[r]>tar:
                        r-=1
                    else:
                        req.append(quad+[nums[l],nums[r]])
                        #for not repeating left index
                        l+=1
                        while l<r and  nums[l]==nums[l-1]:
                            l+=1        
        kSum(4,0,target)
        return req