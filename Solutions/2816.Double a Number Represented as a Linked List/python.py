# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, head: ListNode):
        if head == None:    return 0, None
        nextcarry, nexthead = self.helper(head.next)
        currsum = head.val * 2+nextcarry
        curr, carry = currsum%10, currsum//10
        head.val = curr
        return carry, head

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:    return None
        carry, nexthead = self.helper(head)
        if carry != 0:
            newhead = ListNode(carry, nexthead)
            return newhead
        return head
