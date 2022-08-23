class RandomizedSet:

    def __init__(self):
        self.dic={}
        self.numList=[]
    def insert(self, val: int) -> bool:
        req = val not in self.dic
        if req:
            self.dic[val]=len(self.numList)
            self.numList.append(val)
        
        return req
    def remove(self, val: int) -> bool:
        req = val in self.dic
        if req:
            index=self.dic[val]
            lastval=self.numList[-1]
            self.numList[index]=lastval
            self.numList.pop()
            self.dic[lastval]=index
            del self.dic[val]
        return req
    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()