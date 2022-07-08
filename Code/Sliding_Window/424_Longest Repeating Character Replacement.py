class Solution:
    def character(self, s: str, k: int) -> int:
        s=s.lower()
        dic={}
        req=0
        l=0
        maxf=0
        for r in range(len(s)):
            dic[s[r]]=dic.get(s[r],0)+1
            maxf=max(maxf,dic[s[r]])
            while r-l+1-maxf>k:
                dic[s[l]]-=1
                l+=1            
            req=max(req,r-l+1)
        return req