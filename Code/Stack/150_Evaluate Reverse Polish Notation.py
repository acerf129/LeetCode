class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                pop2=stack.pop()
                pop1=stack.pop()
                val=operators[c](int(pop1),int(pop2))
                stack.append(val)
        return int(stack[0])