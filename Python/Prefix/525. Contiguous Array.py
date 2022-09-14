class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic={0:-1}
        l=0
        maxl=count=0
        for i,v in enumerate(nums):
            if v:
                count+=1
            else:
                count-=1
            if count in dic:
                maxl=max(maxl,i-dic[count]) 
            else:
                dic[count]=i
        return maxl