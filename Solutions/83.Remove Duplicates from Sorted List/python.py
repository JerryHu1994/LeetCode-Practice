# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        curr = head
        if curr != None:
            s.add(curr.val)
        else:
            return
        while curr != None and curr.next != None:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                s.add(curr.next.val)
                curr = curr.next
        return head
        