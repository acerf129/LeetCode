class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        @lru_cache(None)
        def check(word):
            start=0
            for c in word:
                start=s.find(c,start)+1
                if not start:
                    return False
            return True
        return sum(check(word) for word in words)