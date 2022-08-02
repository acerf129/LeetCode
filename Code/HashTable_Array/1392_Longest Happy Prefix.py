class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix=""
        suffix=""
        req=0
        res=""
        n=len(s)
        #0 1 2 3 
        for i in range(n-1):
            if prefix:
                prefix+=s[i]
            else:
                prefix=s[i]
            if suffix:
                suffix=s[n-i-1]+suffix
            else:
                suffix=s[n-i-1]
            if prefix==suffix:
                if len(prefix)>req:
                    req=len(prefix)
                    res=prefix
        return res