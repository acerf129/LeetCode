class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def vow(word):
            return "".join('*' if c in 'aeiou' else c for c in word)
        
        words_p=set(wordlist)
        words_c={}
        words_v={}
        for word in wordlist:
            wordlow=word.lower()
            words_c.setdefault(wordlow,word)
            words_v.setdefault(vow(wordlow),word)
        def solve(query):
            if query in words_p:
                return query
            queryL=query.lower()
            if queryL in words_c:
                return words_c[queryL]
            queryv=vow(queryL)
            if queryv in words_v:
                return words_v[queryv]
            return ""
        req=map(solve,queries)
        return req