class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)
        for i in range(rows-2,-1,-1):
            for j in range(i,-1,-1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
        
        dp=[0]*(len(triangle)+1)#for first row
        
        for row in range(len(triangle)-1,-1,-1):
            for i,v in enumerate(triangle[row]):
                dp[i]=v+min(dp[i],dp[i+1])
                print(dp)
                #4 1 8 3  0
                #7 6 10 3 0 
                #9 10 10 3 0
                #11 10 10 3 0

        return dp[0]