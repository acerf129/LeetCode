# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        req=[]
        
        def dfs(root,height):
            if not root:
                return None
            if height>=len(req):
                req.append([])
            left=dfs(root.left,height+1)
            right=dfs(root.right,height+1)
                          
            req[height].append(root.val)
            return 
        dfs(root,0)
        return req