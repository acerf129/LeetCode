class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for n in nums:
            if not count:
                candidate=n
            count+=1 if n==candidate else -1
        return candidate