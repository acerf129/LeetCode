class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf')]*n for i in range(n)]
        for i in range(n):
            dist[i][i]=0
        for fr,to ,di in edges:
            dist[fr][to]=di
            dist[to][fr]=di
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))
        mincity=0
        maxcity=n
        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=maxcity:
                mincity=i
                maxcity=count
        return mincity