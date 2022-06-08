# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        req={}
        res=[]
        self.count=0
        def dfs(root):
            if not root or self.count:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            
            val=root.val+left+right
            req[val]=req.get(val,0)+1
            return val
        dfs(root)
        frequent=max(req.values())
        for i,k in enumerate(req.items()):
            if frequent==1:
                res.append(k[0])
            elif k[1]==frequent:
                res.append(k[0])
        return res