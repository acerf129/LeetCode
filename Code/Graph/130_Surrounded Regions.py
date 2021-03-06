class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit=set()
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or board[r][c]=="X" or (r,c) in visit:
                return 
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)            
            return    
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit:
                    board[r][c]="X"