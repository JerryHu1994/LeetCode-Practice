# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr, l, fourth = head, 0, None
        while curr != None:
            l += 1
            curr = curr.next
            if curr != None and curr.next == None:
                fourth = curr
        if l==0:    return head
        k = k%l
        if k==0:    return head
        curr = head
        for i in range(l-k-1):
            curr = curr.next
        second = curr
        third = second.next
        # change the order
        fourth.next = head
        second.next = None
        return third
        