class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        check={i:[] for i in range(n)}
        for i,j in edges:
            check[i].append(j)
            check[j].append(i)
        queue=deque([source])
        visit=set([source])
        while queue:
            val=queue.popleft()
            if val==destination:
                return True
            for node in check[val]:                
                if node not in visit:                    
                    queue.append(node)
                    visit.add(node)
        return destination in visit