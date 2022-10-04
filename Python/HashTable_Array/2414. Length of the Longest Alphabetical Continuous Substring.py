class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        hashs=set()
        l=0
        req=1
        for r in range(1,len(s)):
            if ord(s[r])==ord(s[r-1])+1:
                if r-l+1>req:
                    #print(r,l)
                    req=r-l+1
            else:
                l=r
        return req