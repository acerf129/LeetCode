class Solution:
    def reverseBits(self, n: int) -> int:
        req=0
        for i in range(32):
            bit=n>>i&1
            req=req|bit<<31-i
        return req
        
        req=0
        for i in range(32):
            req=req<<1
            bit=n%2
            req+=bit
            n=n>>1
        return req