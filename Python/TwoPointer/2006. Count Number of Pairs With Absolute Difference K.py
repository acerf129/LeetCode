class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:        
        n=len(nums)
        if n==1:
            return 0
        check=defaultdict(int)
        res=0
        for i,v in enumerate(nums):
            res+=check[v+k]
            res+=check[v-k]
            check[v]+=1
        return res