# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,cur=dummy,head
        check=set()
        while cur:
            if cur.val in check:
                prev.next=cur.next
            else:
                prev=cur
            check.add(cur.val)
            cur=cur.next
        return dummy.next