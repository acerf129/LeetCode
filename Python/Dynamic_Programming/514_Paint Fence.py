class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        # write your code here
        if n==0:
            return 0
        same,diff=0,k
        for i in range(n-1):
            temp=diff
            diff=(k-1)*(same+diff)
            same=temp
        return same+diff