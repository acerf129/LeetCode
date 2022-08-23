class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)
        dis=defaultdict(set)
        minHeap=[[0,1]]#d,node
        req=0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        while minHeap:
            d,node=heapq.heappop(minHeap)
            if len(dis[node])>=2:
                continue
            if d in dis[node]:
                continue
            dis[node].add(d)
            q,r =divmod(d,change)
            if q%2:
                d+=change-r
            for nei in adj[node]:
                if nei==n:
                    if req:
                        if d+time!=req:
                            return d+time
                    else:
                        req=d+time                
                if len(dis[nei])<2:
                    heapq.heappush(minHeap,[d+time,nei])