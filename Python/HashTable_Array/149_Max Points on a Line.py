class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return len(points)
        dic={}
        check={}
        req=0
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                val=0
                if points[i][0]-points[j][0]==0:
                    val=float('inf')
                else:
                    val=(points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                if val not in check:
                    check[val]=set()
                check[val].add(i)
                check[val].add(j)
                dic[val]=dic.get(val,0)+1
            for i,v in enumerate(check.items()):
                req=max(req,len(v[1]))
            check={}
        return req
        
        #y=ax+b
        #a+b=4
        #a+b=1