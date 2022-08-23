class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        req=[]
        req.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]>req[-1][1]:
                req.append(intervals[i])
            else:
                minv=min(req[-1][0],intervals[i][0])
                maxv=max(req[-1][1],intervals[i][1])
                req[-1]=[minv,maxv]
        return req