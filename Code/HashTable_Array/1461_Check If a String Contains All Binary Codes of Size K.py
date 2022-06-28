class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #2 option 
        dic={}
        req=[]
        for i,c in enumerate(s):
            req.append(c)
            if  len(req)%k==0:                
                val="".join(req)
                dic[val]=1
                req.pop(0)
        if len(dic)!=2**k:
            return False
        
        return True