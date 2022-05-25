class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Create the rows for the first then
        #items= last line j-1 + lastline j
        rows=[[0]*(i+1)for i in range(numRows)]
        for line in range(numRows):
            for j in range(line+1):
                if j==0 or j==line:
                    rows[line][j]=1
                else:
                    rows[line][j]=rows[line-1][j-1]+rows[line-1][j]
        return rows

        #C line j= C line j-1 * line-j / j
        rows=[[0]*(i+1)for i in range(numRows)]
        
        for line in range(1,numRows+1):
            c=1
            for j in range(1,line+1):
                rows[line-1][j-1]=c
                c=int(c*(line-j)/j)
        return rows
