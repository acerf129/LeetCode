class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for p in ops:
            if p.isdigit()or (p[0]=="-"and p[1:].isdigit()):
                stack.append(int(p))
            elif p=="C":
                stack.pop()
            elif p=="D":
                val=stack[-1]*2
                stack.append(val)
            elif p=="+":
                p1=stack[-1]
                p2=stack[-2]
                stack.append(p1+p2)
        return sum(stack)