class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=="1":
            return False
        req=[False]*len(s)
        req[0]=True
        ##DP
        for c in range(len(s)):
            if req[c] and s[c]=="0":
                cmin = c+minJump
                cmax=c+maxJump            
                if cmin<len(s) :
                    if cmax>=len(s)-1:
                        return True
                    for j in range(cmax,cmin-1,-1):
                        if  req[j]:
                            break
                        else:
                            req[j]=True
        return req[-1]