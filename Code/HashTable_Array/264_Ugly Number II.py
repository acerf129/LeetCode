class Solution:
    def nthUglyNumber(self, n: int) -> int:
        req=[]
        req.append(1)
        #one two three five
        t,th,f=0,0,0
        #index +=1 when num% 235
        #req append when index*235
        for i in range(1,n):
            two=req[t]*2
            three=req[th]*3
            five=req[f]*5
            req.append(min(two,three,five))
            
            if req[i]%2==0:
                t+=1
            if req[i]%3==0:
                th+=1
            if req[i]%5==0:
                f+=1
        return req[-1]