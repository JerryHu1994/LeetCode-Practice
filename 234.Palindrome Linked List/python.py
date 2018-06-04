# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next ==None:    return True
        # find the middle, pointed by left
        left, right = head, head
        while right != None and right.next != None:
            left, right = left.next, right.next.next
        # flip the right half
        slow, fast = left, left.next
        slow.next = None
        while fast != None:
            temp = fast.next
            fast.next = slow
            slow, fast = fast, temp
        # traverse and verify
        l, r = head, slow
        while l != None and r != None:
            if l.val != r.val:
                return False
            l, r = l.next, r.next
        return True
        