# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1!=None or l2!=None or carry:
            s = carry
            if l1!=None:
                s += l1.val
                l1 = l1.next
            if l2!=None:
                s+= l2.val
                l2 = l2.next
            carry = s/10
            newnode = ListNode(s - carry*10)
            curr.next = newnode
            curr = curr.next
        return dummy.next
            
        