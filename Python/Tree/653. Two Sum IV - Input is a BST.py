# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        check={}
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if k-node.val in check:
                return True
            check[node.val]=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False