class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)
        #reverse order
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)
        #[1 2 4 3]
        #lis[2]=1
        #lis[3]=1
        #lis 2 =max(1,1+lis[3]XX)=1
        #lis1=max(1,1+lis[2],1+lis[3])=2
        #lis0=max(1,1+1,1+1,1+2)=3
        #O n2