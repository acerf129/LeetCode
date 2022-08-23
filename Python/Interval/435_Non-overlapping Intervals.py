class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        req=[intervals[0]]
        count=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<req[-1][1]:
                count+=1

                req[-1][1]=min(req[-1][1],intervals[i][1])
            else:
                req.append(intervals[i])
        return count