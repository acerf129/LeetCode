# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1,root2):
            if not root1 and not root2:
                return None
            if not root1 :
                return root2
            if not root2:
                return root1
            
            root1.val=root1.val+root2.val
            root1.left=dfs(root1.left,root2.left)
            root1.right=dfs(root1.right,root2.right)
            return root1
        return dfs(root1,root2)
            
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        v1=root1.val if root1 else 0
        v2=root2.val if root2 else 0
        cur=TreeNode(v1+v2)
        cur.left=self.mergeTrees(root1.left,root2.left)
        cur.right=self.mergeTrees(root1.right,root2.right)
        return cur