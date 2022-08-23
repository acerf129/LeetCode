class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        #for x interger
        #x*(x+1)/2:1,2,3
        #n-(x*(x+1)/2)%x==0 and n>=(x*(x+1)/2) even 
        #n==3 or not 1 + 2 + 3 
        req=0
        i=1
        while i*(i+1)/2<=n:
            v=int((i*(i+1)/2))
            print(i,v,(n-v)%i)
            if (n-v)%i==0:                
                req+=1
            i+=1
        return req