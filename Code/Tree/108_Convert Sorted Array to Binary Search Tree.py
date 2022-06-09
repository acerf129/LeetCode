# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def bst(l,r):
            if l>r:
                return None
            
            mid= (l+r)//2
            
            cur = TreeNode(nums[mid])
            cur.left=bst(l,mid-1)
            cur.right=bst(mid+1,r)
            return cur
        return bst(0,len(nums)-1)