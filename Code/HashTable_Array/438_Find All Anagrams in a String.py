class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        count={}
        dic={}
        meet=0
        req=[]
        for c in p:
            count[c]=count.get(c,0)+1        
        for c in range(len(p)):
            dic[s[c]]=dic.get(s[c],0)+1
            if s[c]in count:
                if dic[s[c]]==count[s[c]]:
                    meet+=1
        if meet==len(count):
            req.append(0)
        l=0
        for i in range(len(p),len(s)):
            dic[s[l]]-=1
            if s[l]in count:
                if dic[s[l]]==count[s[l]]-1:
                    meet-=1                
            dic[s[i]]=dic.get(s[i],0)+1
            if s[i] in count:
                if dic[s[i]]==count[s[i]]:
                    meet+=1
            if meet==len(count):
                req.append(l+1)
            l+=1
        return req