"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic={}
        
        def dfs(node):
            if node in dic:
                return dic[node]
            copy=Node(node.val)
            dic[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return dic[node]
        return dfs(node) if node else None