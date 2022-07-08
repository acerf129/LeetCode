class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio=[]
        for w,h in rectangles:
            ratio.append(w/h)
        req=0
        count=Counter(ratio)
        for i,v in count.items():
            val=v-1
            if val:
                req+=(val+1)*val//2
        return req