# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node=root
        queue=deque()
        queue.append([node,0])
        while queue:
            node2,level=queue.popleft()
            
            if node2.left:
                queue.append([node2.left,level+1])
            if node2.right:
                queue.append([node2.right,level+1])
            
        return root