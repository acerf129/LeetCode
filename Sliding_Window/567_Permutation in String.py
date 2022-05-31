class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count=[0]*26 
        s2Count=[0]*26
        match=0
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        
        for j in range(26):
            match+=1 if s1Count[j]==s2Count[j]else 0
        l=0
        for r in range(len(s1),len(s2)):
            if match==26:
                return True
            #right
            index=ord(s2[r])-ord('a')
            s2Count[index]+=1
            if s1Count[index]==s2Count[index]:
                match+=1
            elif s1Count[index]+1==s2Count[index]:
                match-=1
            #left
            index=ord(s2[l])-ord('a')
            s2Count[index]-=1
            if s1Count[index]==s2Count[index]:
                match+=1
            elif s1Count[index]-1==s2Count[index]:
                match-=1
            l+=1 
        return match==26