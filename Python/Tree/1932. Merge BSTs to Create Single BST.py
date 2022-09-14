# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaf_v=set()
        root_v={}
        for node in trees:
            if node.left:
                leaf_v.add(node.left.val)
            if node.right:
                leaf_v.add(node.right.val)
            root_v[node.val]=node
        root=None
        for node in trees:
            if node.val not in leaf_v:
                if not root:
                    root=node
                else:
                    root=None
        if not root:
            return None
        del root_v[root.val]
        queue=deque()
        queue.append([root,float('-inf'),float('inf')])
        while queue:
            node,left,right=queue.popleft()
            if not (left<node.val<right):
                return None
            if node.left:
                if node.left.val in root_v:
                    node.left=root_v[node.left.val]
                    del root_v[node.left.val]
                queue.append([node.left,left,node.val])
            if node.right:
                if node.right.val in root_v:
                    node.right=root_v[node.right.val]
                    del root_v[node.right.val]
                queue.append([node.right,node.val,right])
        return root if not root_v else None
            
            
            
            
            
            
            
            