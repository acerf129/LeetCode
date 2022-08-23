class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        check={}
        count=0
        for n in nums:
            check[n]=check.get(n,0)+1
            if n-diff in check and n-diff-diff in check:
                count+=1
        return count