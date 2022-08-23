class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        position=set()
        row,col=len(board),len(board[0])
        def backtrack(i,j,k):
            
            if i<0 or j<0 or i==row or j==col or (i,j)in position or board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            position.add((i,j))
            req=(
            backtrack(i+1,j,k+1)or 
            backtrack(i-1,j,k+1)or 
            backtrack(i,j+1,k+1)or 
            backtrack(i,j-1,k+1)
            )
            position.remove((i,j))
            
            return req
        for r in range(row):
            for c in range(col):
                if backtrack(r,c,0):
                    return True
        return False