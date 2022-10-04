class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
        return max(max(row) for row in dp)