class Solution:
    def partition(self, s: str) -> List[List[str]]:
        req=[]
        part=[]
        def backtrack(i):
            if i==len(s):
                req.append(part.copy())
                return 
            for j in range(i,len(s)):
                if palindrome(s,i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
            return             
        def palindrome(s,i,j):
            while i<=j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        backtrack(0)
        return req