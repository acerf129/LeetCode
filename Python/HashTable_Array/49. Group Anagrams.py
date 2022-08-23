class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for s in strs:
            s2="".join(sorted(s))
            if s2 not in dic:
                dic[s2]=[s]
            else:
                dic[s2].append(s)
        return dic.values()
            