class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        unlock=[]
        opens=[]
        for i ,c in enumerate(s):
            if locked[i]=="0":
                unlock.append(i)
            else:
                if s[i]=="(":
                    opens.append(i)
                else:
                    if opens:
                        opens.pop()
                    elif unlock:
                        unlock.pop()
                    else:
                        return False
        #if there is open check the rest
        while opens:
            if unlock and unlock[-1]>opens[-1]:
                opens.pop()
                unlock.pop()
            else:
                return False
        return True