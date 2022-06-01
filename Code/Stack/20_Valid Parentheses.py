class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        start,end={"(":0,"{":1,"[":2},{")":0,"}":1,"]":2}
        req=[]
        for c in s:
            if c in start:
                req.append(c)
            else:                
                if req and start[req[-1]] ==end[c]:
                    req.pop()
                else:
                    return False
        return req==[]