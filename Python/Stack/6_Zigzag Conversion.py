class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        stack=[[]for i in range(numRows)]
        index=0
        check=False
        for i,c in enumerate(s):
            stack[index].append(c)
            if index==0:
                index=1
                check=False
            elif index==numRows-1:
                index=numRows-2
                check=True
            elif check:
                index-=1
            else:                
                index+=1
        req=""
        for c in stack:
            req+="".join(c)
        return req