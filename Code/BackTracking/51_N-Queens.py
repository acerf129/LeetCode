class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cur=[["."]*n for i in range(n)]
        col,positiveDiag,negtiveDiag=set(),set(),set()
        req=[]

        def backtrack(i):
            if i==n :
                
                copys=["".join(i) for i in cur]
                req.append(copys)   
                return
            
            for j in range(n):
                if j in col or (i+j) in positiveDiag or (i-j) in negtiveDiag:
                    continue
                col.add(j)
                positiveDiag.add((i+j))
                negtiveDiag.add((i-j))
                cur[i][j]="Q"
                backtrack(i+1)
                cur[i][j]="."
                col.remove(j)
                positiveDiag.remove((i+j))
                negtiveDiag.remove((i-j))            
            return
        backtrack(0)
        return req