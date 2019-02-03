# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        while curr != None:
            n = curr.next
            if n==curr: return True
            curr.next = curr
            curr = n
        return False
            
        