# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a,b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next
            
            