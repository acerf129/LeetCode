class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==len(cardPoints):
            return sum(cardPoints)
        stack=cardPoints[-k:]
        req=sum(stack)
        cur=req
        for i in range(k):
            cur-=stack.pop(0)
            cur+=cardPoints[i]
            req=max(req,cur)        
        return req