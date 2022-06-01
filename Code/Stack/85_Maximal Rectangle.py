class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # raw matrix 10100
        #            10111
        #            11111
        #            10010
        # matrix
        #           10100
        #           10123
        #           12345
        #           10010
        if len(matrix)==0:
            return 0
        rows,cols=len(matrix),len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                matrix[r][c]=1 if matrix[r][c]=="1"else 0
                if matrix[r][c]==1 and c>=1 and matrix[r][c-1]>0:
                    matrix[r][c]=matrix[r][c-1]+1
        req,monostack=0,deque()
        for c in range(cols):#col by col search max area
            monostack.clear()
            for r in range(rows):
                r2=r
                while len(monostack)>0 and matrix[r][c]<monostack[-1][0]:
                    val,r2=monostack.pop()
                    req=max(req,val*(r-r2))
                monostack.append((matrix[r][c],r2))
            while len(monostack)>0:
                val,r2=monostack.pop()
                req=max(req,val*(rows-r2))
        return req
    
    
    
    