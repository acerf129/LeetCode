class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:      
        #DFS  
        visit={}
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
            return 0
        def dfs(r,c):
            if r==rows or c==cols:
                return 0
            if r==rows-1 and c==cols-1:
                return 1            
            if (r,c)in visit:
                return visit[(r,c)]
            if obstacleGrid[r][c]==1:
                visit[(r,c)]=0
                return 0
            res=dfs(r+1,c)
            res+=dfs(r,c+1)
            visit[(r,c)]=res
            return res
        return dfs(0,0)
        #BFS
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,rows):
            #face obstacle or not
            obstacleGrid[i][0]= int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        for i in range(1,cols):
            #face obstacle or not
            obstacleGrid[0][i]= int(obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1)
        
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[rows-1][cols-1]