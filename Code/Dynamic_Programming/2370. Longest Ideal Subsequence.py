class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n=len(s)
        if k==25:
            return n
        count=[0]*26
        for c in s:
            index=ord(c)-ord('a')
            minindex=max(index-k,0)
            maxindex=min(index+k,25)
            count[index]=max(count[minindex:maxindex+1])+1
        return max(count)
        