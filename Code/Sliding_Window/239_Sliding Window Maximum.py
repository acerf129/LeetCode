class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        req=[]
        l,r=0,0
        while r<len(nums):
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                req.append(nums[q[0]])
                l+=1
            r+=1
        return req