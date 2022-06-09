class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
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