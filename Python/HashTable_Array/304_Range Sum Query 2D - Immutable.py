class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r==0 and c==0:
                    self.matrix[r][c]=matrix[r][c]
                elif r==0:                    
                    self.matrix[r][c]=matrix[r][c]+self.matrix[r][c-1]
                    
                elif c==0:
                    self.matrix[r][c]=matrix[r][c]+self.matrix[r-1][c]
                else:
                    self.matrix[r][c]=matrix[r][c]+self.matrix[r-1][c]+self.matrix[r][c-1]-self.matrix[r-1][c-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        req=0
        req+=self.matrix[row2][col2]
        if col1>0:
            req-=self.matrix[row2][col1-1]
        if row1>0:
            req-=self.matrix[row1-1][col2]        
        if col1>0 and row1>0:
            req+=self.matrix[row1-1][col1-1]
        return req


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)