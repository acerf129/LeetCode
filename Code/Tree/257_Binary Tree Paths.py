# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        req=[]
        
        def dfs(root,curs):
            if not root.left and not root.right:
                req.append("->".join(curs))
                return

            if root.left:                
                left=dfs(root.left,curs+[str(root.left.val)])
            if root.right:                
                right=dfs(root.right,curs+[str(root.right.val)])
            return
            
        dfs(root,[str(root.val)])
        return req