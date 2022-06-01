class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count=[0]*26
        s2count=[0]*26
        match=0
        l=0
        #start from 0 to s1 len
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        #check the match
        for r in range(26):
            if s1count[r]==s2count[r]:
                match+=1
        #start from s1 len to s2 len
        for r in range(len(s1),len(s2)):
            if match==26:
                return True
            #move right
            index=ord(s2[r])-ord('a')
            s2count[index]+=1
            if s2count[index]==s1count[index]:
                match+=1
            elif s2count[index]-1==s1count[index]:
                match-=1            
            #move left 
            index=ord(s2[l])-ord('a')
            s2count[index]-=1
            if s2count[index]==s1count[index]:
                match+=1
            elif s2count[index]+1==s1count[index]:
                match-=1
            l+=1
        return match==26