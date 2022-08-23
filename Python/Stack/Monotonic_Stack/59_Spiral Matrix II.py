class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up,down,left,right=0,n,0,n
        stack=[]
        req=[[]*i for i in range(n)]
        count=1
        while up<down and left<right:
            for i in range(left,right):
                stack.append([count,up,i])
                count+=1
            up+=1
            for i in range(up,down):
                stack.append([count,i,right-1])
                count+=1
            right-=1
            if not (up<down and left<right):                
                break
            for i in range(right-1,left-1,-1):
                stack.append([count,down-1,i])
                count+=1
            down-=1
            for i in range(down-1,up-1,-1):
                stack.append([count,i,left])
                count+=1
            left+=1
        for v,i,j in  sorted(stack,key=lambda x:[x[1],x[2]]):
            req[i].append(v)
        return req