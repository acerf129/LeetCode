from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.interval=SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start in self.interval:
            return False
        keys=self.interval.keys()
        
        key=bisect.bisect_left(keys,start)
        #print(key)
        if key>0 and self.interval[keys[key-1]]>start:#end>start
            return False
        if key<len(keys) and keys[key]<end:
            return False
        self.interval[start]=end
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)