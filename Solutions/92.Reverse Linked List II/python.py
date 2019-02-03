# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # nav to pre
        for i in range(m-1):
            pre = pre.next
        curr, currnext = pre.next, pre.next.next
        for i in range(n-m):
            temp = currnext.next
            currnext.next = curr
            curr, currnext = currnext, temp
        first = pre.next
        pre.next, first.next = curr, currnext
        return dummy.next