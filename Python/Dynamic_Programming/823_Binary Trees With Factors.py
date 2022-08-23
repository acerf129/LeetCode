class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod=(10**9+7)
        cache={}
        arr.sort()
        for i,v in enumerate(arr):
            cache[v]=i        
        lens=len(arr)
        dp=[1]*lens
        #2 5 10. 0 2 3
        for i in range(lens):
            for j in range(i):
                if arr[i]%arr[j]==0:               
                    right=arr[i]/arr[j]
                    if right in cache:
                        dp[i]+=dp[j]*dp[cache[right]]
                        dp[i]%=mod
        return sum(dp)%mod