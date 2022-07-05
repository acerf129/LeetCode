class Solution:
    def candy(self, ratings: List[int]) -> int:
        count=0
        prefix=[1]*len(ratings)
        suffix=[1]*len(ratings)
        stack=[]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                prefix[i]=prefix[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                suffix[i]= suffix[i+1]+1
        for i in range(len(prefix)):
            val=max(prefix[i],suffix[i])
            stack.append(val)
        return sum(stack)