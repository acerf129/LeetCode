class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            res=[0]*26
            for l in word:
                res[ord(l)-ord('a')]+=1
            return res
        word2=[0]*26
        req=[]
        for word in words2:
            for i,v in enumerate(count(word)):
                word2[i]=max(word2[i],v)
        
        for word in words1:
            if all(x>=y for x,y in zip(count(word),word2)):
                req.append(word)
        return req