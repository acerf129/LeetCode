# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        req=[True,0]
        def dfs(root,cur):
            if not root  :
                cur=[True,0]
                return cur
            left=dfs(root.left,cur)
            right=dfs(root.right,cur)

            balance=abs(left[1]-right[1])<=1 and left[0] and right[0]
            cur=[balance,1+max(left[1],right[1])]
            return cur
        
        return dfs(root,req)[0]