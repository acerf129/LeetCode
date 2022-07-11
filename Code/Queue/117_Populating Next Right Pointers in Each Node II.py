"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue=deque()
        queue.append(root)
        while queue:
            temp=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                print(cur.val)
                if cur.left:
                    queue.append(cur.left)
                    temp.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    temp.append(cur.right)
            print(temp)
            for j in range(len(temp)-1):
                temp[j].next=temp[j+1]
        return root