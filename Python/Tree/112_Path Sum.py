# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,cur):
            if not root:
                return False
            curSum=cur+root.val
            if curSum==targetSum and not root.left and not root.right:
                return True
            left = dfs(root.left,curSum)
            right =dfs(root.right,curSum)
            return left or right
        return dfs(root,0)