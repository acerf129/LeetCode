class Solution:
    def findConnected(self,n:int, edges: List[List[int]]) -> List[int]:
        parent={i:[] for i in range(n)}
        rank=[i for i in range(n)]
        count=n
        def find(node):
            p=parent[node]
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        
        for n1,n2 in edges:
            if  union(i-1,i):
                count-=1
        return count