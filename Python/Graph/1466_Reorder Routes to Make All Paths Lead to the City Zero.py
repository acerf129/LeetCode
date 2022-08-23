class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges={(a,b) for a,b in connections}
        nMap={i:[] for i in range(n)}
        for fr,to in connections:
            nMap[fr].append(to)
            nMap[to].append(fr)
        visit=set()
        def dfs(node):
            if node in visit:
                return 0
            visit.add(node)      
            req=0
            for nei in nMap[node]:
                if nei in visit:
                    continue
                if (nei,node)not in edges:
                    req+=1
                req+=dfs(nei)            
            return req
        return dfs(0)