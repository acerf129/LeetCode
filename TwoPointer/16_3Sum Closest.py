class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        req=float('inf')
        mini=float('inf')
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]>target:
                    if (nums[i]+nums[l]+nums[r])-target<mini:
                        mini=(nums[i]+nums[l]+nums[r])-target
                        req=(nums[i]+nums[l]+nums[r])
                    r-=1
                elif nums[i]+nums[l]+nums[r]<target:       
                    if target-(nums[i]+nums[l]+nums[r])<mini:
                        mini=target-(nums[i]+nums[l]+nums[r])
                        req=(nums[i]+nums[l]+nums[r])
                    l+=1
                else:
                    return nums[i]+nums[l]+nums[r]
        return req