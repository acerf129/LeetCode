class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        while p%2==0 and q%2==0:
            p/=2
            q/=2
        
        if q%2 and p%2:
            return 1
        if p%2==0 and q%2:
            return 2
        return 0