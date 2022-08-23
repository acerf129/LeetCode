class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic={}
        for i,w in enumerate(wall):
            for j,v in enumerate(w):
                if j!=0:
                    wall[i][j]+=wall[i][j-1]
                dic[wall[i][j]]=dic.get(wall[i][j],0)+1
        if len(dic)==1:
            return max(dic.values())
        for i,v in enumerate(sorted(dic.values(),reverse=True)):
            if i==1:
                return len(wall)-v