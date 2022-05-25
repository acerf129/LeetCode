class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #.   1111111 Intuitive way
        dp=[[0]*n for i in range(m)]
        for i in range(n):
            dp[m-1][i]=1
        for j in range(m):
            dp[j][n-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        rows=[1]*n
        for i in range(m-1):
            for j in range(n-2,-1,-1):
                rows[j]+=rows[j+1]
        return rows[0]

    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n
        for i in range(m-1):
            for j in range(n-2,-1,-1):
                row[j]+=row[j+1]
        return row[0]