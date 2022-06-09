# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #val > left
        #val<right
        def valid (root,left,right):
            if not root:
                return True
            if not (root.val<right and root.val>left):
                return False
            left=valid(root.left,left,root.val)
            right=valid(root.right,root.val,right)
            return left and right
        return valid(root,float('-inf'),float('inf'))
    
# go left update the right
# go right update the left