class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dica={}
        dicb={}        
        for i in s:
            dica[i] = dica.get(i,0)+1
        for j in t:
            dicb[j] = dicb.get(j,0)+1
        return dica==dicb