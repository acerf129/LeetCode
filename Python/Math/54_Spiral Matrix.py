class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bot,left,right=0,len(matrix),0,len(matrix[0])
        req=[]
        
        while left<right and top<bot:
            for i in range(left,right):
                req.append(matrix[top][i])
            top+=1
            for i in range(top,bot):
                req.append(matrix[i][right-1])
            right-=1
            
            if not left<right or not top<bot:
                break
                
            for i in range(right-1,left-1,-1):
                req.append(matrix[bot-1][i])
            bot-=1
            for i in range(bot-1,top-1,-1):
                req.append(matrix[i][left])
            left+=1
        return req