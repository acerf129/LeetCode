class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
                
        cur=0
        start,end=[[i,v[1]] for i,v in enumerate(trips)],[[i,v[2]] for i,v in enumerate(trips)]
        start.sort(key=lambda x:x[1])
        end.sort(key=lambda x:x[1])
        
        l,r=0,0
        while l<len(start) and r<len(end):            
            if start[l][1]<end[r][1]:
                index=start[l][0]
                cur+=trips[index][0]
                l+=1
            elif start[l][1]>end[r][1]:
                index=end[r][0]
                cur-=trips[index][0]
                r+=1
            else:
                index=start[l][0]
                cur+=trips[index][0]
                l+=1
                index=end[r][0]
                cur-=trips[index][0]
                r+=1
            if cur>capacity:
                return False
        return True