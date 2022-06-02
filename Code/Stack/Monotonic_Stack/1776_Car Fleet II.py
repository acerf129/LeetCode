class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        #remain the slower one
            
        req=[-1]*len(cars)
        stack=[]
        
        for i in range(len(cars)-1,-1,-1):
            while stack:
                index=stack[-1]
                #faster speed pop or cur time > right time
                if cars[index][1]>=cars[i][1] or ((cars[index][0]-cars[i][0])/(cars[i][1]-cars[index][1])>req[index] and req[index]>0):
                    #faster pop
                    stack.pop()               
                else:
                    req[i]=(cars[index][0]-cars[i][0])/(cars[i][1]-cars[index][1])
                    break
            
            stack.append(i)
        return req