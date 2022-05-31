class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        charset=set()
        l=0
        req=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            req=max(req,r-l+1)
        return req