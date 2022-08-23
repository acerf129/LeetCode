class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count=set()
        
        for n in triplets:
            if len(count)==3:
                break
            if n[0]>target[0] or n[1]>target[1]or n[2]>target[2]:
                continue
            for i in range(len(n)):
                if n[i]==target[i]:
                    count.add(i)            
        return True if len(count)==3 else False