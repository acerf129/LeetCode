# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=cur=ListNode(0,head)
        
        def getk(curr,k):
            while curr and k:
                curr=curr.next
                k-=1
            return curr
        while True:            
            knode=getk(cur,k)
            if not knode:
                break                
            #reverse node here    
            knext=knode.next#3
            prev=knext#3
            curr=cur.next#1
            while curr!=knext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            #set cur to 1
            temp=cur.next
            cur.next=knode
            cur=temp                
            #
        return dummy.next