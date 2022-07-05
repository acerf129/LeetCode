class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)!=0:
                prefix=prefix[0:len(prefix)-1]
            if not prefix:
                return ""
        return prefix

        if not strs:
            return ""
        def isCommonPrefix(lens):
            str1=strs[0][:lens]
            for i in range(1,len(strs)):
                if strs[i].find(str1)!=0:
                    return False
            return True
        
        minLen=float("inf")
        for s in strs:
            minLen=min(minLen,len(s))
        low,high=1,minLen
        while low<=high:
            middle=(low+high)//2
            if isCommonPrefix(middle):
                low=middle+1
            else:
                high=middle-1
        print(low,high)
        return strs[0][:(low+high)//2]