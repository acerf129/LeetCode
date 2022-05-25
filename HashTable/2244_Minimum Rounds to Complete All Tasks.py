class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        req=0
        dic={}
        for i in range(len(tasks)):
            v=tasks[i]
            dic[v]=dic.get(v,0)+1
        for i,key in enumerate(dic):
            if dic[key]==1:
                return -1
            divtime=dic[key]//3
            remain=dic[key]%3
            
            if dic[key]==2:
                req+=1
            elif remain==2:
                req+=divtime+1
            elif remain==1:
                req+=divtime-1+2
            else:
                req+=divtime
        return req