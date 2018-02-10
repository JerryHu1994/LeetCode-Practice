# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:    return head
        odd, even, evenhead = head, head.next, head.next
        while even!=None and even.next!=None:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenhead
        return head