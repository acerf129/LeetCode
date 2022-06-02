# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=ListNode(0,head)
        prev=None
        cur=start.next
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev