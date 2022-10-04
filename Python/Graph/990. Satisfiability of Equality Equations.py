#Union Find
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rank=[1]*26
        parent=[i for i in range(26)]
        def find(x):
            p=x
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                parent[p2]=p1
            else:
                rank[p2]+=rank[p1]
                parent[p1]=p2
            
        for a,e,_,b in equations:
            if e=="=":
                a=ord(a)-ord('a')
                b=ord(b)-ord('a')
                union(a,b)
        for a,e,_,b in equations:
            if e=="!" :
                a=ord(a)-ord('a')
                b=ord(b)-ord('a')
                if find(parent[a])==find(parent[b]):
                    return False
        return True