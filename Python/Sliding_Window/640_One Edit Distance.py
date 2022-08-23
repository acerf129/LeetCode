def is_one_edit_distance(self, s: str, t: str) -> bool:
        # write your code here
        if s==t:
            return False        
        if abs(len(s)-len(t))>=2:
            return False
        if len(s)>len(t):
            s,t=t,s
        minLen=min(len(s),len(t))
        l,r=0,minLen-1
        #print(minLen)
        while l<minLen and s[l]==t[l]:
            l+=1
        if len(s)==len(t):
            while r>-1  and s[r]==t[r]:
                r-=1
        else:
            while r>-1  and s[r]==t[r+1]:
                r-=1
        #tea #det 
        return l==r or r<0 or l==minLen or (s[l:r+1]==t[l:r+1] or s[l+1:r+2]==t[l+1:r+2])