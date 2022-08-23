class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific top left
        #atlantic right bot
        req=[]
        pacific=set()
        atlantic=set()
        rows,cols=len(heights),len(heights[0])
        def dfs(r,c,ocean,prevH):
            if r<0 or c<0 or r==rows or c==cols or (r,c)in ocean or heights[r][c]<prevH:
                return
            #if not smaller than prev add in set
            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])
            return 
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    req.append([r,c])
        return req