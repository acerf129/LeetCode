# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        req=[]
        def dfs(root):
            if not root:
                return None
            req.append(root.val)
            left=dfs(root.left)
            right=dfs(root.right)
            return root.val
        dfs(root)
        return req