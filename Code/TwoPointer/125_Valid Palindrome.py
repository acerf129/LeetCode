#isalpha isalnum isnumeric
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        req=""
        news=s.lower()
        for c in news:
            if c.isalnum():
                req+=c   
            else:
                continue
        return req[::-1]==req