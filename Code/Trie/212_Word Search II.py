class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        cur=self
        for w in word:
            if w not in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.isWord=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        
        for w in words:
            root.addWord(w)
        rows,cols = len(board),len(board[0])
        req,visit=set(),set()
        
        def dfs(r,c,node,word):
            if( r<0 or c<0 or r==rows or c==cols or 
               (r,c)in visit or board[r][c] not in node.children):
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                req.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
            return 
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(req)