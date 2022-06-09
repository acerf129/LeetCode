# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        req=[]
        def dfs(root):
            if not root:
                req.append("N")
                return 
            req.append(str(root.val))
            left=dfs(root.left)
            right=dfs(root.right)
            return 
            
        dfs(root)
        sreq=",".join(req)#list to string
        return sreq

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0#index of the list
        req = data.split(",")#string to list
        def dfs():
            if req[self.i]=="N":
                self.i+=1
                return None
            node= TreeNode(int(req[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()     
            return node
            
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))