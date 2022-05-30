class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        req=""
        for s in strs:
            req+=str(len(s))+"#"+s
        return req
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        req,i=[],0
        while i<len(str):
            j=i
            while  j<len(str) and str[j]!="#" :
                j+=1
            length=int(str[i:j])
            req.append(str[j+1:j+1+length])
            i=j+1+length
        return req