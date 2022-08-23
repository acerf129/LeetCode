# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        req=[root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=leftMax if leftMax>0 else 0
            rightMax=rightMax if rightMax>0 else 0
            req[0]=max(req[0],root.val+leftMax+rightMax)
            return root.val+max(leftMax,rightMax)
            
        dfs(root)
        return req[0]