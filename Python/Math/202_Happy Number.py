class Solution:
    def isHappy(self, n: int) -> bool:
        check=set()        
        while n not in check:
            check.add(n)
            temp=n
            req=0
            while temp:
                val=temp%10
                req+=val**2
                temp=temp//10
            n=req
            if n==1:
                return True
        return False