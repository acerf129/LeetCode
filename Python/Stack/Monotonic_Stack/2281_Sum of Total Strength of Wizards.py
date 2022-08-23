class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod=(10**9+7)
        lens=len(strength)
        #prefix for sum
        #monotonic for left small right small
        prefix=list(accumulate(accumulate(strength,initial=0)))
        left,right=[-1]*lens,[lens]*lens
        stack=[]
        req=0
        #right small
        for i in range(lens):
            while stack and strength[stack[-1]]>strength[i]:
                index=stack.pop()
                right[index]=i
            stack.append(i)
        #left small
        stack=[]
        for i in range(lens-1,-1,-1):
            while stack and strength[stack[-1]]>=strength[i]:
                index=stack.pop()
                left[index]=i
            stack.append(i)
        
        for i in range(lens):
            l,r=left[i],right[i]
            laccu,raccu=prefix[i]-prefix[max(l,0)],prefix[r]-prefix[i]
            ln,rn=i-l,r-i
            req+=strength[i]*(raccu*ln-laccu*rn)
            
        return req%mod