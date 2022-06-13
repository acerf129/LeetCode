class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isWord=True
    def search(self, word: str) -> bool:
        cur=self.root
        
        def dfs(i,cur):
            print(i)
            for j in range(i,len(word)):
                if word[j]==".":
                    for k in cur.children.values():
                        #skip the node
                        if dfs(j+1,k):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur=cur.children[word[j]]
            return cur.isWord
        
        return dfs(0,cur)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)