class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        req=0
        l=0
        for i in range(1,n+1):
            
            if i&(i-1)==0:
                l+=1
            req=((req<<l)|i)%mod
        return req