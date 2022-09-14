class Solution:
    def partitionString(self, s: str) -> int:
        req=0
        s2=''
        for c in s:
            if c in s2:
                s2=''
                req+=1
            if c not in s2:
                s2+=c
                
        return req+1