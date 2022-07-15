class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2)>len(nums1):
            nums2,nums1=nums1,nums2
        m,n=len(nums1),len(nums2)
        req=0
        for r in range(-n+1,m+n-1):
            count=0
            for l in range(n):
                p1=r+l
                if p1<0:
                    continue
                if p1>=m:
                    break
                
                if nums1[p1]==nums2[l]:
                    count+=1
                    if count>req:
                        req=count
                else:
                    count=0
        return req

        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
        return max(max(row) for row in dp)