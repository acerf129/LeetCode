class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        req=[]
        cur=[]
        if len(s)>12:
            return req
        
        
        def backTrack(i,dot):
            if i==len(s) and dot==4:
                val="".join(cur)
                val=val[:len(val)-1]
                req.append(val)
                return
            if dot>4:
                return 
            for j in range(i, min(i+3,len(s))):
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    vals=s[i:j+1]+"."
                    cur.append(vals)
                    backTrack(j+1,dot+1)
                    cur.pop()
            return 
        backTrack(0,0)
        return req