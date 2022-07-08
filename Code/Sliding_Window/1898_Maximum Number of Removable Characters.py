class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        req=0
        removed=set()
        def isSubseq(s,subseq):
            i1,i2=0,0
            while i1<len(s) and i2<len(subseq):
                if i1 in removed or s[i1]!=subseq[i2]:
                    i1+=1
                    continue
                i1+=1
                i2+=1
            return  i2==len(subseq)
        l,r=0,len(removable)-1
        while l<=r:
            middle=(l+r)//2
            
            removed=set(removable[:middle+1])
            print(removed)
            if isSubseq(s,p):
                req=max(req,middle+1)
                l=middle+1
            else:
                r=middle-1
        return req