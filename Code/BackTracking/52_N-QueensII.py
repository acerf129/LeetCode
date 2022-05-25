class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        positiveDiag=set()
        negtiveDiag=set()
        def backtrack(r):
            if r==n:
                return 1
            req=0
            for c in range(n):
                if c in cols or (r+c) in  positiveDiag  or (r-c)in negtiveDiag:
                    continue
                cols.add(c)
                positiveDiag.add(r+c)
                negtiveDiag.add(r-c)
                req+=backtrack(r+1)
                
                cols.remove(c)
                positiveDiag.remove(r+c)
                negtiveDiag.remove(r-c)
            return req
        
        return backtrack(0)