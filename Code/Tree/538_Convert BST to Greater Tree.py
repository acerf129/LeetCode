# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.curSum=0
        def dfs(root):
            if not root:
                return 0
            
            right=dfs(root.right)
            temp=root.val
            root.val+=self.curSum
            self.curSum+=temp
            left=dfs(root.left)            
            return 
        dfs(root)   
        return root