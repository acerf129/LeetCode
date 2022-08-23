class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        check={}
        directions=[[0,1],[1,0],[0,-1],[-1,0]]#NESW right
        way=0
        check[(0,0)]=1     
        i,j=0,0
        for ins in instructions:
            if ins=="G":
                i,j=i+directions[way][0],j+directions[way][1]
                if (i,j) not in check:
                    check[(i,j)]=1
                else:
                    check[(i,j)]+=1
            else:
                if ins=="R":
                    way+=1
                    if way==len(directions):
                        way=0
                else:
                    way-=1
                    if way==-1:
                        way=len(directions)-1
        return (i,j)==(0,0) or directions[way]!=[0,1]