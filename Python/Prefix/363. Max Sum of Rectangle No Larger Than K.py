class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows,cols=len(matrix),len(matrix[0])
        req=float(-inf)
        for l in range(cols):
            rowSum=[0]*rows
            for r in range(l,cols):
                colSums=[0]
                colSum=0
                for i in range(rows):
                     # sum up rowSum in each row from i to j, use prefix sum to speed up
                    rowSum[i]+=matrix[i][r]
                    # sum up rows up to r
                    colSum+=rowSum[i]
                    diff=colSum-k
                    # find the smallest element larger than colSum-k if exists
                    index=bisect_left(colSums,diff)
                    if index<len(colSums):
                        if colSums[index]==diff:
                            return k
                        else:
                            req=max(req,colSum-colSums[index])
                    insort(colSums,colSum)
        return req