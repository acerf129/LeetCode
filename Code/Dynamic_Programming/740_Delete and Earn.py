class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums=list(set(nums))
        earn1,earn2=0,0
        #e1 e2
        #check the anount of pick #if nums-1==i-1  anount+ e1 else +e2
        for i in range(len(nums)):
            amount = nums[i]*count[nums[i]]
            if i>0 and nums[i]-1==nums[i-1]:
                temp=earn2
                earn2=max(amount+earn1,earn2)
                earn1=temp
            else:
                temp=earn2
                earn2=max(amount+earn2,earn2)
                earn1=temp
        return earn2