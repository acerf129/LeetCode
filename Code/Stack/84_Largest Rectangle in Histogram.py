class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        stack=[]
        req=0
        rows,cols=len(matrix),len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                matrix[r][c]=1 if matrix[r][c]=="1" else 0 
                if c>0 and matrix[r][c]==1 and matrix[r][c-1]!=0:
                    matrix[r][c]+=matrix[r][c-1]
                    
        for c in range(cols):#from col to check the value 
            stack=[]
            for r in range(rows):
                r2=r
                while stack and matrix[r][c]<stack[-1][1]:
                    r2,val=stack.pop()
                    req=max(req,(r-r2)*val)
                stack.append((r2,matrix[r][c]))
            while stack:#count the straight val
                r2,val=stack.pop()
                req=max(req,(rows-r2)*val)
        return req