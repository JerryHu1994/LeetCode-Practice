# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:    return None
        last = head
        while last.next != None:    last = last.next
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        # reverse the second half
        curr, pre = head2, None
        while curr:
            nex = curr.next
            curr.next = pre
            pre = curr
            curr = nex
        # combine and merge
        curr1, curr2 = head1, pre
        while curr2:
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1, curr2 = next1, next2