# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(left,right):
            if left==right-1:
                return [TreeNode(left)]
            elif left>right-1:
                return [None]
            else:
                tree=[]
                for nums in range(left,right):
                    for l in dfs(left,nums):
                        for r in dfs(nums+1,right):
                            root=TreeNode(nums)
                            root.left=l
                            root.right=r
                            tree.append(root)
                return tree
        
        return dfs(1,n+1)