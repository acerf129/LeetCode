class FreqStack:

    def __init__(self):
        self.maxval=0
        self.hash={}
        self.count={}
    def push(self, val: int) -> None:
        self.count[val]=self.count.get(val,0)+1
        if self.count[val]>self.maxval:
            self.maxval+=1
            self.hash[self.maxval]=[]
        self.hash[self.count[val]].append(val)
    def pop(self) -> int:
        val=len(self.hash[self.maxval])
        req=self.hash[self.maxval].pop()
        self.count[req]-=1
        if val==1:
            self.maxval-=1
        return req


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()