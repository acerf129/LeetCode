class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #means move three times 
        #compare 4th and 5th difference
        if len(nums)<=4:
            return 0
        nums.sort()
        req=[]
        #3 time right
        #3 time left
        #2 left 1 right
        #2 right 1 left
        req.append(nums[-4]-nums[0])
        req.append(nums[-1]-nums[3])
        req.append(nums[-2]-nums[2])
        req.append(nums[-3]-nums[1])
        return min(req)

        if len(nums)<=4:
            return 0
        maxheap=[-n for n in nums]
        minheap=[n for n in nums]
        heapq.heapify(maxheap)
        heapq.heapify(minheap)
        maxh=[]
        minh=[]
        for i in range(4):
            maxh.append(-heapq.heappop(maxheap))
            minh.append(heapq.heappop(minheap))
        minh=minh[::-1]
        return min([i-j for i,j in zip(maxh,minh) ])