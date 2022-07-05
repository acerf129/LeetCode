class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:        
        stack=s.split(" ")
        if len(stack)!=len(pattern):
            return False
        dic={}
        check=set()
        for i,p in enumerate(pattern):
            if p not in dic:
                if stack[i] not in check:
                    dic[p]=stack[i]
                    check.add(stack[i])
                else:
                    return False
            else:
                if stack[i]!=dic[p]:
                    return False
        return True