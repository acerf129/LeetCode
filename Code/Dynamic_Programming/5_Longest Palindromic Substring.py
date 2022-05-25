class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    resLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    resLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res
        
        res=""
        resLen=0
        i=0
        #pointer 
        while i<len(s):
            j,k=i,i
            while k+1<len(s) and s[k]==s[k+1]:
                k+=1
            i=k+1
            while k+1<len(s) and j>0 and s[k+1]==s[j-1]:
                j-=1
                k+=1
            if k-j+1>resLen:
                resLen=k-j+1
                res=s[j:k+1]      
        return res