class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicts={}
        req=float('inf')
        for i in range(len(nums)):
            if nums[i] not in dicts:
                dicts[nums[i]]=i
            else:
                req=min(req, abs(i-dicts[nums[i]]))
                dicts[nums[i]]=i
        return req<=k