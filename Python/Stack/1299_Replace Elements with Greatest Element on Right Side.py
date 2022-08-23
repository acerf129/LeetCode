class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax=-1
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            stack.append(curMax)
            curMax=max(curMax,arr[i])
        return stack[::-1]