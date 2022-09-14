class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        count1={}
        count2={}
        for i in range(n):
            if s[i] not in count1 and t[i] not in count2:
                count1[s[i]]=t[i]
                count2[t[i]]=s[i]
            elif count1.get(s[i])!=t[i] or count2.get(t[i])!=s[i]:
                return False
        return True