class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        lps=[0]*len(needle)
        
        prev,i=0,1
        
        while i<len(needle):
            if needle[i]==needle[prev]:
                lps[i]=prev+1
                prev+=1
                i+=1
            else:
                if prev==0:
                    lps[i]=0
                    i+=1
                else:
                    prev=lps[prev-1]
        i,j=0,0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                if j==0:                    
                    i+=1
                else:
                    j=lps[j-1]
            if  j==len(needle):
                return i-len(needle)
        return -1