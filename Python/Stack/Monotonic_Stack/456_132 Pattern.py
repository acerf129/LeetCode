class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]#pair [num,minleft]
        curMin=nums[0]
        #i<k<j move the k
        for n in nums[1:]:
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack and n>stack[-1][1] and n<stack[-1][0]:
                return True
            curMin=min(curMin,n)
            stack.append([n,curMin])
        return False