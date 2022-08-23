class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def backTrack(s):
            if s==s[::-1]:
                return 0
            req=float('inf')
            
            for j in range(len(s)):
                if s[:j+1]==s[:j+1][::-1]:
                    req=min(req,1+backTrack(s[j+1:]))
            return req
        return backTrack(s)

        n=len(s)
        dp=[n]*n
        dp[n-1]=0 
        
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True     
        if isPalindrome(0,n-1):
            return 0
        
        for i in range(1,n):
            if isPalindrome(0,i-1) and isPalindrome(i,n-1):
                return 1
        #s[i:j] if true go s[j+1]   
        for i in range(n-1,-1,-1):            
            for j in range(i,n):
                if isPalindrome(i,j):       
                    if j+1==n:
                        dp[i]=0
                    else:
                        dp[i]=min(dp[i],1+dp[j+1])
        return dp[0]