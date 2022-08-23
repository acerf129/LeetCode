class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        req=0
        n=len(s)
        
        for unique in range(1,27):# kinds of char
            count=[0]*26
            i=0
            cur_unique=0
            valid_unique=0
            for j in range(len(s)):
                #add to right
                cur=ord(s[j])-ord('a')
                count[cur]+=1
                if count[cur]==1:
                    cur_unique+=1
                if count[cur]==k:
                    valid_unique+=1
                #shrink by left
                while cur_unique>unique:
                    cur=ord(s[i])-ord('a')
                    count[cur]-=1
                    if count[cur]==0:
                        cur_unique-=1
                    if count[cur]==k-1:
                        valid_unique-=1
                    i+=1
                if valid_unique==unique:
                    req=max(req,j-i+1)
        return req