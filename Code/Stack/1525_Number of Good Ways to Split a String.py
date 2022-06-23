class Solution:
    def numSplits(self, s: str) -> int:
        count1={}
        count2=Counter(s)
        count=0
        
        for i in range(len(s)):
            count1[s[i]]=count1.get(s[i],0)+1
            if s[i] in count2 and count2[s[i]]>1:
                count2[s[i]]-=1
            else:
                del count2[s[i]]
            if len(count1)==len(count2):
                count+=1
        return count