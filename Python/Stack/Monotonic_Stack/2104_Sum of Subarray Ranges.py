class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        lens=len(nums)
        lefts=[-1]*lens
        rights=[lens]*lens
        leftl=[-1]*lens
        rightl=[lens]*lens
        req=0
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                index=stack.pop()
                rights[index]=i
            stack.append(i)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                index=stack.pop()
                lefts[index]=i
            stack.append(i)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                index=stack.pop()
                rightl[index]=i
            stack.append(i)
        stack=[]    
        
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                index=stack.pop()
                leftl[index]=i
            stack.append(i)
        for i in range(lens):
            lefti=lefts[i]
            righti=rights[i]
            leftj=leftl[i]
            rightj=rightl[i]
            small=nums[i]*(i-lefti)*(righti-i)
            large=nums[i]*(i-leftj)*(rightj-i)
            req+=large-small
        return req