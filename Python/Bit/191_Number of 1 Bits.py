class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        req=0
        while n:
            req+=n%2
            n=n>>1
        return req