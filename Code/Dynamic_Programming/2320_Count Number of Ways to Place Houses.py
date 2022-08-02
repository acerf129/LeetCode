class Solution:
    def countHousePlacements(self, n: int) -> int:
        one,two=1,1
        mod=(10**9+7)
        for i in range(n):
            temp=one+two
            two=one%mod
            one=temp%mod
        return one*one%mod
            