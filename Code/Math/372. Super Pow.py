class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        def helper(a,b):
            if a==0:
                return 0
            if b==0 or a==1:
                return 1
            req=helper(a*a,b//2)%1337
            return req*a if b%2 else req
        req=1
        for x in b:
            req=helper(req,10)*helper(a,x)%1337
        return req

        if a==1:
            return 1
        val=0
        for v in b:
            val=val*10+v
        return pow(a,val,1337)
