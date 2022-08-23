class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        req=[]
        for p in people:
            req.insert(p[1],p)
        return req
        
        queue=[[-1,-1]]*len(people)
        people.sort()
        for i,j in people:
            place,taller=0,0
            
            while taller<j:
                if queue[place][0]>=i or queue[place][0]==-1:
                    place+=1
                    taller+=1
                else:
                    place+=1
            while queue[place][0]!=-1:
                place+=1            
            queue[place]=[i,j]
        return queue