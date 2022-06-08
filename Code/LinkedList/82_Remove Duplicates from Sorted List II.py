# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check={}
        dummy=ListNode(0,head)
        
        prev,cur=dummy,head
        
        while cur:
            if cur.val in check:
                check[cur.val]=check.get(cur.val,0)+1
                prev.next=cur.next
                cur=cur.next
                continue            
            check[cur.val]=check.get(cur.val,0)+1
            prev=cur
            cur=cur.next
        prev,cur=dummy,head
        while cur:
            if  check[cur.val]>1:
                prev.next=cur.next
                cur=cur.next
                continue            
            prev=cur
            cur=cur.next
        return(dummy.next)