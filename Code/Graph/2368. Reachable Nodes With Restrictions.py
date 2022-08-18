class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj={i:[] for i in range(n)}
        count=Counter(restricted)
        print(count)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #bfs
        queue=deque()
        queue.append(0)#node
        visit=set()
        visit.add(0)
        while queue:
            node=queue.popleft()    
            temp=adj[node].copy()
            for nei in adj[node]:
                if nei in count:
                    temp.remove(nei)
                    continue
                if nei not in visit and nei not in count:
                    visit.add(nei)
                    temp.remove(nei)
                    queue.append(nei)
            adj[node]=temp
        return len(visit)