class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[-1]
        arr.append(0)
        req=0
        for i2,v in enumerate(arr):
            while stack and v<arr[stack[-1]]:
                i=stack.pop()
                i1=stack[-1]
                val=(i-i1)*(i2-i)*arr[i]
                req+=val
            stack.append(i2)
            
        return req%(10**9+7)