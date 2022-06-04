"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={None:None}#node with node store val at first
        
        cur=head
        while cur:
            dic[cur]=Node(cur.val)
            cur=cur.next
        
        cur=head
        
        while cur:
            dic[cur].next=dic[cur.next]
            dic[cur].random=dic[cur.random]
            cur=cur.next
        return dic[head]