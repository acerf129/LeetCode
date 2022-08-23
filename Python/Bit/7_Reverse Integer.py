class Solution:
    def reverse(self, x: int) -> int:
        maxs=2**31-1
        mins=-(2**31)
        req=0
        while x:
            digit=int(math.fmod(x,10))#-1 %10
            x=int(x/10)#-1 /10
            if (req>maxs//10) or (req==maxs//10 and digit>=maxs%10):
                return 0
            if (req<mins//10) or (req==mins//10 and digit<=mins%10):
                return 0
            req=req*10+digit
        return req