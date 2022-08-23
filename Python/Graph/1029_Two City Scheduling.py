class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cache={}
        half=len(costs)//2
        def dfs(i,acount,bcount):
            if i==len(costs):
                return 0
            if (i,acount,bcount) in cache:
                return cache[(i,acount,bcount)]
            cache[(i,acount,bcount)]=float('inf')
            req1=min(cache[(i,acount,bcount)],dfs(i+1,acount+1,bcount)+costs[i][0])if acount<half else float('inf')
            req2=min(cache[(i,acount,bcount)],dfs(i+1,acount,bcount+1)+costs[i][1])if bcount<half else float('inf')
            req= req1 if req1<req2 else req2
            cache[(i,acount,bcount)]=req
            return req
        return dfs(0,0,0)
        req=0
        diff=[]
        for c1,c2 in costs:
            diff.append([c2-c1,c1,c2])
        diff.sort()
        for i in range(len(diff)):
            if i<len(diff)//2:
                req+=diff[i][2]
            else:
                req+=diff[i][1]
        return req