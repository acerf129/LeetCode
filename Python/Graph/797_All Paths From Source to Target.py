class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        req=[]
        dic={i:[] for i in range(len(graph))}
        for i,v in enumerate(graph):
            for j in v:
                dic[i].append(j)
        def dfs(i,temp):
            if i==len(graph)-1:
                temp.append(i)
                req.append(temp.copy())
                temp.pop()
                return 
            temp.append(i)
            for nei in graph[i]:
                dfs(nei,temp)
            temp.pop()
            return 
        dfs(0,[])        
        return req