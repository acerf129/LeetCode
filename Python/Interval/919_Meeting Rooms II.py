class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        req=0
        count=0
        starts=[i.start for i in intervals]
        ends=[i.end for i in intervals]
        starts.sort()
        ends.sort()
        i,j=0,0
        while i<len(starts):
            if starts[i]<ends[j]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            req=max(req,count)
        return req