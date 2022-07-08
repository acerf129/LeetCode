class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,req=set(),set()
        
        for i in range(len(s)-9):
            cur=s[i:i+10]
            if cur in seen:
                req.add(cur)
            else:
                seen.add(cur)
        return list(req)