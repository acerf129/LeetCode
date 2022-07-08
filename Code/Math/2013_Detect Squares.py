class DetectSquares:

    def __init__(self):
        self.ptcount=collections.defaultdict(int)
        self.points=[]
    def add(self, point: List[int]) -> None:
        self.ptcount[tuple(point)]+=1
        self.points.append(point)
    def count(self, point: List[int]) -> int:
        px,py=point
        req=0
        for x,y in self.points:
            if abs(py-y)!=abs(px-x) or x==px or y==py:
                continue
            #get diagonal
            req+= self.ptcount[(x,py)]* self.ptcount[(px,y)]
        return req

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)