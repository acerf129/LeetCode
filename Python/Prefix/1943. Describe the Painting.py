class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:             
        dic=collections.defaultdict(int)
        for i,j,c in segments:
            dic[i]+=c
            dic[j]-=c
        req=[]
        i=0
        for j in sorted(dic):
            if dic[i]:
                req.append([i,j,dic[i]])
            dic[j]+=dic[i]
            i=j
        
        return req