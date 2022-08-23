class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        req=[]
        n=len(scores)
        for i in range(n):
            req.append([ages[i],scores[i]])
        req.sort()
        dp=[0]*n
        total=0
        print(req)
        #increasing if the cur >=last dp[i]+....if req[i]>=req[j]
        for i in range(n):
            dp[i]=req[i][1]
            for j in range(i):
                if req[j][1]<=req[i][1]:                    
                    dp[i]=max(dp[i],dp[j]+req[i][1])
            total=max(total,dp[i])
        print(dp)
        return total