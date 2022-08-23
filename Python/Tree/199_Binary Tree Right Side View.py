# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        req=[]
        check=set()
        def dfs(root,height):
            if not root:
                return 0
            if height not in check:
                check.add(height)
                req.append(root.val)
            right=dfs(root.right,1+height)
            left=dfs(root.left,1+height)
            
            return 1+max(left,right)
        dfs(root,0)
        return req