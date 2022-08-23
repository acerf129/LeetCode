class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0"==num1 or "0"==num2:
            return "0"
        
        req=[0]*(len(num1)+len(num2))
        n1=num1[::-1]
        n2=num2[::-1]
        for i in range(len(n1)):
            for j in range(len(n2)):
                req[i+j]+=int(n1[i])*int(n2[j])
                req[i+j+1]+=req[i+j]//10
                req[i+j]%=10
        req=req[::-1]
        res=0
        for v in req:
            res=res*10+v
        return str(res)