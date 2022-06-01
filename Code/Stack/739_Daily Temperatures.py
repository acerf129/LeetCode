class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stacks with index value
        #new index - index if thevalue> stack value
        stack=[]
        req=[0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and v>stack[-1][1]:
                index,value=stack.pop()
                req[index]=i-index
            stack.append((i,v))
        return req