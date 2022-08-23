class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        
        nodes=[set() for i in range(n)]
        req=[]
        temp=[]
        remain=n
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)          
        for i in range(len(nodes)):
            if len(nodes[i])==1:
                temp.append(i)
        
        while remain>2:
            remain-=len(temp)
            newtemp=[]
            while temp:
                leaf=temp.pop()#3
                node=nodes[leaf].pop()
                nodes[node].remove(leaf)
                if len(nodes[node])==1:
                    newtemp.append(node)
            temp=newtemp
        return temp
            
            