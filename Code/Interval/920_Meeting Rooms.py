from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if len(intervals)<=1:
            return True
        l,r=0,0
        for i in range(len(intervals)):
            if intervals[i].start<r and intervals[i].start>l:
                return False
            l=intervals[i].start
            r=intervals[i].end
        return True