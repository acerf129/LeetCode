class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        req=[]
        
        for i in range(len(intervals)):
            # 2 3 4 5
            if newInterval[1]<intervals[i][0]:
                req.append(newInterval)
                return req+intervals[i:]
            #4 5.  2 3
            elif newInterval[0]>intervals[i][1]:
                req.append(intervals[i])
            else:
                minv=min(newInterval[0],intervals[i][0])
                maxv=max(newInterval[1],intervals[i][1])
                newInterval=[minv,maxv]
        req.append(newInterval)
        return req