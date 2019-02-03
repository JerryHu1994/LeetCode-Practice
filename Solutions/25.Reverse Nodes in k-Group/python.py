# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:  return head
        # check if there is k nodes left
        curr = head
        for i in range(k):
            if not curr:    return head
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        first, second, third = head, head.next, head.next.next
        for i in range(k-1):
            second.next = first
            first, second = second, third
            if third:  third = third.next
        dummy.next = first
        head.next = self.reverseKGroup(second, k)
        return dummy.next