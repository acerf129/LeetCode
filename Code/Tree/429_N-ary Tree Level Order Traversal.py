"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        req=[[]]
        queue=deque()
        queue.append([root,0])
        while queue:
            node,level=queue.popleft()
            if level==len(req):
                req.append([])
            req[level].append(node.val)
            if node.children:
                for ch in node.children:
                    queue.append([ch,level+1])                       
        return req