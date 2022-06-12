# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        req=[0]
        check=set()
        def dfs(root,height):
            if not root:
                return None
            if height not in check:
                check.add(height)
                req[0]=root.val
            left=dfs(root.left,height+1)
            right=dfs(root.right,height+1)
            return root
        dfs(root,0)
        return req[0]