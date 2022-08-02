class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        visit=set()
        for i in range(len(nums)):
            local=set()
            while True:
                if i in local:
                    return True
                if i in visit:
                    break
                local.add(i)
                visit.add(i)
                prev=i
                i=(i+nums[i])%n
                if prev==i or (nums[i]>0)!=(nums[prev]>0):
                    break
        return False