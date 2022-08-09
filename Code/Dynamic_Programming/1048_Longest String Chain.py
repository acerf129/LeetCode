class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compare(w1,w2):
            if len(w1)!=len(w2)+1:
                return False
            l,r=0,0
            while l<len(w1):
                if r<len(w2) and w1[l]==w2[r]:
                    l+=1
                    r+=1
                else:
                    l+=1
                if l==len(w1) and  r==len(w2):
                    return True
            return False
            
            
        words.sort(key=len)
        req=0
        lens=len(words)
        dp=[1 for i in range(lens)]
        for i in range(lens):
            for prev in range(i):
                if compare(words[i],words[prev]) and dp[i]<dp[prev]+1:
                    dp[i]=dp[prev]+1
        return max(dp)
            