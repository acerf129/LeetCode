class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dic={}
        dic2={}
        req=[]
        check=[]
        meet=True
        for i,c in enumerate(pattern):
            if c not in dic:
                dic[c]=[]
            dic[c].append(i)
        
        for v in dic.values():
            check.append(v)
        for word in words:
            dic2={}
            for i,c in enumerate(word):
                if c not in dic2:
                    dic2[c]=[]
                dic2[c].append(i)
            if len(dic)==len(dic2):    
                meet=True
                for i,v in enumerate(dic2.values()):
                    if v!=check[i]:
                        meet=False
                        break
                if meet:
                    req.append(word)
                    
        return req