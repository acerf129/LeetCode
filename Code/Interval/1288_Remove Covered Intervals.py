class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:(i[0],-i[1]))
        req=0
        left,right=intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=left and intervals[i][1]<=right or(intervals[i][0]<=left and intervals[i][1]>=right ):
                req+=1
            else:
                left=intervals[i][0]
                right=intervals[i][1]
        return len(intervals)-req
    
    
    # c a b d