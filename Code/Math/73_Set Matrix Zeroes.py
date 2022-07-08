class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        row=set()
        col=set()
        
        for i in range((rows)):
            for j in range((cols)):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for c in range(cols):
                matrix[i][c]=0
                
        for j in col:
            for r in range(rows):
                matrix[r][j]=0