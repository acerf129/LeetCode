# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left= self.minDepth(root.left)
        right=self.minDepth(root.right)
        if not left:
            left=right
        if not right:
            right=left
        return 1+min(left,right)

        if not root:
            return 0
        queue=deque()
        queue.append([1,root])
        req=float('inf')
        while queue:
            level,node=queue.popleft()
            if node.left:
                queue.append([level+1,node.left])
            if node.right:
                queue.append([level+1,node.right])
            if not node.left and not node.right:
                req=min(req,level)
        return req if req!=float('inf') else 1