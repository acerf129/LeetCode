class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        visit=set()
        for word in words:
            temp=""
            for c in word:
                index=ord(c)-ord('a')
                temp+=morse[index]
            if temp not in visit:
                visit.add(temp)
        return len(visit)