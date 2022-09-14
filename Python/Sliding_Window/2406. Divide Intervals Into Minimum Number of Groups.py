class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A=[]
        for f,t in intervals:
            A.append([f,1])
            A.append([t+1,-1])
        A.sort()
        req,cur=0,0
        for f,diff in A:
            cur+=diff
            req=max(req,cur)
        return req