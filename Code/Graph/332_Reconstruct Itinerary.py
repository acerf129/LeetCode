class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tripMap={fr:[] for fr,to in tickets}
        tickets.sort()
        for fr,to in tickets:
            tripMap[fr].append(to)
        req=[]
        
        req.append("JFK")
        def dfs(fr):
            if len(req)==len(tickets)+1:
                return True
            if fr not in tripMap:
                return False
            temp=list(tripMap[fr])
            for index,value in enumerate(temp):
                tripMap[fr].pop(index)
                req.append(value)
                if dfs(value):
                    return True
                req.pop()
                tripMap[fr].insert(index,value)
            return False
        dfs("JFK")
        return req        