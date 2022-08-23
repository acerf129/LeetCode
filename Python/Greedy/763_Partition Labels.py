class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={}
        req=[]
        for i,c in enumerate(s):
            lastIndex[c]=i
        size,end=0,0
        for i in range(len(s)):
            size+=1
            if lastIndex[s[i]]>end:
                end=lastIndex[s[i]]
                
            if i==end:
                req.append(size)
                size=0
        return req