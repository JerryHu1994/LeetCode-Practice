# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        largeHead, smallHead = ListNode(0), ListNode(0)
        lcurr, scurr = largeHead, smallHead
        curr = head
        while curr != None:
            if curr.val < x:
                scurr.next = curr
                scurr = scurr.next
            else:
                lcurr.next = curr
                lcurr = lcurr.next
            curr = curr.next
        lcurr.next = None
        scurr.next = largeHead.next
        return smallHead.next