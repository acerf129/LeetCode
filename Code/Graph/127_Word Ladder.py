class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)
        visit=set()
        visit.add(beginWord)
        queue=deque()
        queue.append(beginWord)
        res=1
        while queue:
            for i in range(len(queue)):
                word=queue.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neibor in nei[pattern]:
                        if neibor not in visit:
                            visit.add(neibor)
                            queue.append(neibor)
            res+=1
        return 0