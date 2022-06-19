class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        wordMap={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minLen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    wordMap[w1[j]].add(w2[j])
                    break
        visit={}
        req=[]
        #False means cycle
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c]=False
            for nei in wordMap[c]:
                if not dfs(nei):
                    return False
            visit[c]=True
            req.append(c)
            return True
        for w in sorted(wordMap.keys(),reverse=True):
            if not dfs(w):
                return ""
        req.reverse()
        return "".join(req)