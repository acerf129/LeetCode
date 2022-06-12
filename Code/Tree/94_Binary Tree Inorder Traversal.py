# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        req=[]
        
        def dfs(root):
            if not root:
                return None
            left=dfs(root.left)
            req.append(root.val)
            right=dfs(root.right)
            return root
        dfs(root)
        return req