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
        stack1, stack2 = [], []
        curr1, curr2 = l1, l2
        while curr1!=None:
            stack1.append(curr1.val)
            curr1 = curr1.next
        while curr2!=None:
            stack2.append(curr2.val)
            curr2 = curr2.next
        ret = None
        carry = 0
        while len(stack1)!=0 or len(stack2)!=0:
            val1 = stack1.pop() if len(stack1)!=0 else 0
            val2 = stack2.pop() if len(stack2)!=0 else 0
            currsum = val1 + val2 + carry 
            carry = 1 if currsum >= 10 else 0  
            node = ListNode(currsum%10)
            node.next = ret
            ret = node
        if carry==1:
            node = ListNode(1)
            node.next = ret
            ret = node
        return ret
            
        
        
        