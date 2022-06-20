class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visit={}
        n=len(graph)
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node]=False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visit[node]=True
            return True
        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res