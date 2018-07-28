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
        dummy = ListNode(-1)
        dummy.next = head
        if head == None:    return None
        curr = dummy
        right = dummy.next
        currval = right.val
        currcount = 1
        while right.next != None:
            right = right.next
            if currval == right.val:
                currcount += 1
            else:
                if currcount == 1:
                    curr = curr.next
                else:
                    curr.next = right
                    currcount = 1
                currval = right.val
        # in the end, if the last run has counts larger than one, end it
        if currcount > 1:
            curr.next = None
        return dummy.next
            
            