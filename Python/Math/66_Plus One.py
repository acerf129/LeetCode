class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        req=digits[::-1]
        temp=0
        for i in range(len(req)):
            if i==0:
                req[i]=req[i]+1
                if not req[i]//10:
                    return req[::-1]
                else:
                    temp=1
                    req[i]=req[i]%10
                continue
            req[i]+=temp
            if req[i]//10:
                temp=1
                req[i]=req[i]%10
            else:
                temp=0
        if temp==1:
            req=req+[1]
        return req[::-1]