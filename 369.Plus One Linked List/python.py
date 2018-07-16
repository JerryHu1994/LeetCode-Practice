# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self, h):
        if h.next == None:
            if h.val == 9:
                h.val = 0
                return 1
            else:
                h.val += 1
                return 0
        carry = self.helper(h.next)
        if carry==1:
            if h.val == 9:
                h.val = 0
                return 1
            else:
                h.val += 1
                return 0
        return 0
    
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        front = self.helper(head)
        if front == 1:
            n = ListNode(1)
            n.next = head
            return n
        return head