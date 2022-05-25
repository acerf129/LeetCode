class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        dp=[0,0,0]
        for i in range(len(costs)):
            dp0=costs[i][0]+min(dp[1],dp[2])
            dp1=costs[i][1]+min(dp[0],dp[2])
            dp2=costs[i][2]+min(dp[0],dp[1])
            dp=[dp0,dp1,dp2]
        print(dp)
        return min(dp) 
        cache={}
        def dfs(i,j):
            if i==len(costs):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)]=0
            if j==0:
                cache[(i,j)]=costs[i][0]+min(dfs(i+1,j+1),dfs(i+1,j+2))
            if j==1:
                cache[(i,j)]=costs[i][1]+min(dfs(i+1,j-1),dfs(i+1,j+1))
            if j==2:
                cache[(i,j)]=costs[i][2]+min(dfs(i+1,j-1),dfs(i+1,j-2))
            return cache[(i,j)]
        req=float('inf')
        for i in range(3):
            req=min(req,dfs(0,i))
        return req if req!= float('inf') else 0