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

        l,req=0,0
        dic={}
        for r in range(len(s)):
            while s[r] in dic and dic[s[r]]>0:
                dic[s[l]]-=1
                l+=1
            dic[s[r]]=1
            req=max(req,r-l+1)
        return req