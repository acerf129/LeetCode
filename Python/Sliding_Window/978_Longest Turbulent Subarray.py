class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(a,b):
            if a==b:
                return 0
            elif a>b:
                return 1
            else:
                return -1
        n=len(arr)
        req=1
        cur=0
        for i in range(1,n):
            c=cmp(arr[i-1],arr[i])
            if c==0:
                cur=i
            elif i==n-1 or c*cmp(arr[i],arr[i+1])!=-1:
                req=max(req,i-cur+1)
                cur=i
        return req