# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        curr = head
        while curr != None:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None