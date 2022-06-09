# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,num):
            if not root :
                return 0
            if not root.left and not root.right:
                return num*10+root.val
            num=num*10+root.val
            left = dfs(root.left,num)
            right=dfs(root.right,num)
            return left+right
        return dfs(root,0)
        
        # 12+13