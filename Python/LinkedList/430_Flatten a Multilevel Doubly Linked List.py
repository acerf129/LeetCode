"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        def dfs(node):
            req.append(node)
            if node.child:
                dfs(node.child)
            if node.next:
                dfs(node.next)
        req=[]
        dfs(head)
        for i in range(len(req)-1):
            req[i].next=req[i+1]
            req[i].child=None
            req[i+1].prev=req[i]
        req[-1].next=None
        return req[0]
    
        