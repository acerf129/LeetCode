class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic={}
        word=sorted(words)
        req=""
        res=0
        for w in word:            
            if len(w)==1 or w[0:len(w)-1]  in dic:
                dic[w]=1
                if len(w)>res:
                    res=len(w)
                    req=w
        return req