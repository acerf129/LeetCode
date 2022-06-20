class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000"in deadends:
            return -1
        def children(val):
            req=[]
            for i in range(4):
                newval=str((int(val[i])+1)%10)
                req.append(val[:i]+newval+val[i+1:])
                newval=str((int(val[i])-1)%10)
                req.append(val[:i]+newval+val[i+1:])
            print(req)
            return req
        queue=deque()
        queue.append(["0000",0])
        visit=set(deadends)
        visit.add("0000")
        while queue:
            val,move=queue.popleft()
            if val==target:
                return move
            for child in children(val):
                if child not in visit:
                    visit.add(child)
                    queue.append([child,move+1])
        return -1