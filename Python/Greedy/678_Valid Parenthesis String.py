class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax,leftMin=0,0
        for c in s:
            if c=="(":
                leftMax+=1
                leftMin+=1
            if c=="*":
                leftMax+=1
                leftMin-=1
            if c==")":
                leftMax-=1
                leftMin-=1
            if leftMax<0:
                return False
            if leftMin<0:
                leftMin=0
        return True if leftMax==0 or leftMin ==0 else False
                
            