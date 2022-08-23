# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=req=ListNode(0,None)
        temp=0
        while l1 or l2:
            if l1:
                temp+=l1.val
                l1=l1.next
            if l2:
                temp+=l2.val
                l2=l2.next
            if temp>=10:
                req.val=temp%10
            else:
                req.val=temp
            if (l1 or l2) :
                req.next=ListNode(0,None)            
                req=req.next
            if temp>=10:
                temp=1
            else:
                temp=0
        if temp>0:
            req.next=ListNode()
            req=req.next
            req.val=temp
        return dummy