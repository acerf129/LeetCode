# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.getMid(head)
        rnext=right.next
        right.next=None
        right=rnext
        
        left=self.sortList(left)
        right=self.sortList(right)        
        head=self.merge(left,right)
        return head
        
        
    def getMid(self,head):
        
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def merge(self,left,right):
        
        dummy=cur=ListNode()
        while left and right:
            if left.val<right.val:
                cur.next=left
                left=left.next
            else:
                cur.next=right
                right=right.next
            cur=cur.next
        if left:
            cur.next=left
        if right:
            cur.next=right
        return dummy.next