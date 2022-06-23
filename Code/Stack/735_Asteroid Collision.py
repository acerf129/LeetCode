class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            if ast>0:
                stack.append(ast)
            else:
                # if  ast
                stack.append(ast)
                while  len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                    last1=stack[-1]
                    last2=stack[-2]
                    if abs(last2)>abs(last1):
                        stack.pop()
                    elif abs(last2)<abs(last1):
                        stack.pop(-2)
                    else:
                        stack.pop()
                        stack.pop()
        return stack