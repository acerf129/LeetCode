class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        a,b=a[::-1],b[::-1]
        temp=0
        #11+11
        for i in range(max(len(a),len(b))):
            digita = int(a[i])  if i<len(a)else 0
            digitb=int(b[i])if i<len(b) else 0
            if digita+digitb+temp>=2:
                val=str(digita+digitb+temp-2)
                res+=val
                temp=1
            else:
                res+=str(digita+digitb+temp)
                temp=0
        if temp:
            res+="1"
        return res[::-1]