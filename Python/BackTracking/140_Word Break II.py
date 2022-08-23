
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        req=[]
        
        def backtrack(i=0,cur=[]):
            if i==len(s):
                req.append(" ".join(cur))
                return
            for word in wordDict:
                if i+len(word)<=len(s)and s[i:i+len(word)]==word:
                    cur.append(word)
                    backtrack(i+len(word),cur)
                    cur.pop()
            return
        backtrack()
        return req