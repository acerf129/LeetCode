# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        req=[0]
        
        def dfs(root):
            
            if not root:
                return -1
            left=dfs(root.left)
            right=dfs(root.right)
            
            #diameter edge diameter = ０
            req[0]=max(req[0],2+left+right)
            #height edge height==0

            return 1+max(left,right)

        dfs(root)
        return req[0]