class Solution:
    def findConnected(self,n:int, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(n)]
        rank=[1]*n

        def find(n1):
            p=n1
            while p !=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            else:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        res=n
        for n1,n2 in edges:
            if union(n1, n2):
                res-=1
        return res