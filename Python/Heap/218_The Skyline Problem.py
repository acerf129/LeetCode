from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        height=SortedList()
        buildHeight=[]
        
        for l,r,h in buildings:
            buildHeight.append([l,h])
            buildHeight.append([r,-h])
        buildHeight.sort(key=lambda x:(x[0],-x[1]))

        req=[]
        prev,preh=[-1,-1]
        for p ,h in buildHeight:
            if req:
                prev,preh=req[-1]
            if h<0:
                height.discard(-h)
                if not height:
                    req.append([p,0])
                elif -h==preh and -h!=height[-1]:
                    req.append([p,height[-1]])
            else:
                height.add(h)
                if h>preh:
                    req.append([p,h])
        return req