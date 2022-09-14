class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)
        for f,t,v in shifts:
            if v==0:
                prefix[f]-=1
                prefix[t+1]+=1
            else:
                prefix[f]+=1
                prefix[t+1]-=1
        cur=0
        news=list(s)
        for i in range(len(s)):
            cur+=prefix[i]
            new=(ord(s[i])+cur-ord('a'))%26+ord('a')
            news[i]=chr(new)
        return "".join(news)