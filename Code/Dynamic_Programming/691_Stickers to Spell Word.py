class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickerCount=[]
        for i,v in enumerate(stickers):
            stickerCount.append({})
            for c in v:
                #insert value in dic
                stickerCount[i][c]=stickerCount[i].get(c,0)+1
        dp={}
        #remain character |min sticker count
        def dfs(tar,stick):
            if tar in dp:
                return dp[tar]
            if tar=="":
                return 0
            res=1 if  stick else 0
            remainT=""
            for c in tar:
                if c in stick and stick[c]>0:
                    stick[c]-=1
                else:
                    remainT+=c
            if remainT:
                used=float('inf')
                for s in stickerCount:
                    if remainT[0] not in s:
                        continue
                    used=min(used,dfs(remainT,s.copy()))
                dp[remainT]=used
                res+=dp[remainT]
            return res
            
        #choose empty choose sticker
        res=dfs(target,{})
        return res if res !=float("inf") else -1 