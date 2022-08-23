# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:        
        if not root:
            return 0
        def dfs(root,total):
            if not root:
                return 
            if total==root.val:
                self.count+=1 
            left=dfs(root.left,total-root.val)
            right=dfs(root.right,total-root.val)

            return 
        dfs(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)
        return self.count