class Trie:
    def __init__(self):
        self.count=[None]*26
        self.visited=0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie,a,req=Trie(),ord('a'),[]
        for word in words:
            t=trie
            for c in word:
                c=ord(c)-a
                if not t.count[c]:
                    t.count[c]=Trie()
                t.count[c].visited+=1
                t=t.count[c]
        for x in words:
            t,cur=trie,0
            for c in x:
                c=ord(c)-a
                cur+=t.count[c].visited
                t=t.count[c]
            req.append(cur)
        return req