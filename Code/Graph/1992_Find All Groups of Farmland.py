class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visit=set()
        rows,cols=len(land),len(land[0])
        #rectangle left top right bot 
        req=[]
        
        def dfs(r,c,left,right):
            if r<0 or r==rows or c<0 or c==cols or land[r][c]==0 or (r,c) in visit:
                return             
            #base case
            req[-1]=left+right
            if r>right[0] or c>right[1]:
                right[0],right[1]=r,c
                req[-1]=left+right            
            visit.add((r,c))
            dfs(r+1,c,left,right)
            dfs(r-1,c,left,right)
            dfs(r,c+1,left,right)
            dfs(r,c-1,left,right)
            
            return 
        for r in range (rows):
            for c in range(cols):
                if (r,c) not in visit and land[r][c]==1:
                    req.append([])
                    dfs(r,c,[r,c],[r,c])
        return req