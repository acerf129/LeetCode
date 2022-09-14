class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def move(r:int,c:int,cand:str):
            if any(board[r][j]==cand for j in range(9)):
                return False
            if any(board[j][c]==cand for j in range(9)):
                return False
            br,bc=3*(r//3),3*(c//3)
            if any(board[i][j]==cand for i in range(br,br+3) for j in range(bc,bc+3)) :
                return False
            return True
        def dfs(r,c):
            while board[r][c]!=".":
                c+=1
                if c==9:
                    c=0
                    r+=1
                if r==9:
                    return True
            for i in range(1,10):
                if move(r,c,str(i)):
                    board[r][c]=str(i)
                    if dfs(r,c):
                        return True
                    board[r][c]="."
            return False
        dfs(0,0)