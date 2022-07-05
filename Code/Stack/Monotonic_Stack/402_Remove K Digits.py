class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
        stack=[]
        req=""
        for n in num:
            while stack and stack[-1]>n and k:
                stack.pop()
                k-=1
            stack.append(n)
        
        while stack and stack[0]=="0":
            stack.pop(0)        
        while k and stack:
            stack.pop()
            k-=1
        req="".join(stack)
        
        return req if req else "0"