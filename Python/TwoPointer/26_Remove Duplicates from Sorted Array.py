class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        dup=False
        lens=len(nums)
        for r in range(lens):
            if nums[l]==nums[r]:
                dup=True
                continue
            if dup and nums[l]!=nums[r]:
                l+=1
                nums[l],nums[r]=nums[r],nums[l]
        for k in range(l+1,lens):
            nums[k]=None
        
        return l+1