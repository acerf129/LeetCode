class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s=str(n)
        
        for i in range(len(s)-1,0,-1):
            if s[i-1]>s[i]:
                n=n-(int(s[i:])+1)
                s=str(n)
        return n