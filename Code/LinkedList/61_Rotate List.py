# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        left,right=ListNode(0,head),ListNode(0,head)
        k=k%(self.getLen(head))
        if not k:
            return head
        while k>0:
            right=right.next            
            k-=1
        while right.next:
            left=left.next
            right=right.next
        lnext=left.next
        left.next=None
        right.next=head
        return lnext
        
    def getLen(self,head):
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count