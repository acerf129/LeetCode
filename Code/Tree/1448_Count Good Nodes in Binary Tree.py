# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,num):
            if not root:
                return 0
            #return good node
            check = 1 if root.val>=num else 0
            num = max(num,root.val)
            left=dfs(root.left,num)
            right=dfs(root.right,num)
            return check+left+right
        
        return dfs(root,root.val)