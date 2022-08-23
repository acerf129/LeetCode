# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        req=[]        
        def dfs(root,cur):
            if not root:
                return 
            if sum(cur)==targetSum and not root.left and not root.right:
                req.append(cur)
            
            if root.left:
                dfs(root.left,cur+[root.left.val])
            if root.right:
                dfs(root.right,cur+[root.right.val])
            return 
        dfs(root,[root.val])
        return req