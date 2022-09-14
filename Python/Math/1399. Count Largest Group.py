class Solution:
    def countLargestGroup(self, n: int) -> int:
        req=[]
        for i in range(1,n+1):
            req.append(sum(int(x) for x in str(i)))
        count=Counter(req)
        x=[i for i in count.values() if i==max(count.values())]
        return len(x)