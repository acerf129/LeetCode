class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add open if i<m
        #add close if j <i
        stack=[]
        req=[]
        def dfs(i,j):
            if i==n and j==n:
                req.append("".join(stack))
                return
            if i<n:
                stack.append("(")
                dfs(i+1,j)
                stack.pop()
            if j<i:
                stack.append(")")
                dfs(i,j+1)
                stack.pop()            
        dfs(0,0)
        return req