class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach=[]
        count=0
        for d,s in zip(dist,speed):
            minute=math.ceil(d/s)
            minReach.append(minute)
        minReach.sort()
        for i in range(len(minReach)):
            
            if i>=minReach[i]:
                return count
            count+=1
        return count