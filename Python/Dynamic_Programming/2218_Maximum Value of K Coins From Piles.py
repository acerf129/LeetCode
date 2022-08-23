class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        lens=len(piles)
        
        @cache
        def dfs(n,j):
            if j==lens:
                return 0
            if n==0:
                return 0
            m=-1
            csum=0
            used=0
            for p in piles[j]:
                csum+=p
                used+=1
                m=max(m,csum+dfs(n-used,j+1))
                if used==n:
                    break
            return max(m,dfs(n,j+1))
            
            
        return dfs(k,0)