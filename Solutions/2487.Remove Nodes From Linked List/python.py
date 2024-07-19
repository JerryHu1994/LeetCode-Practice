# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)[1]
            
    def helper(self, h: ListNode):
        if h == None:   return (0, h)
        rightval, righthead = self.helper(h.next)
        if h.val >= rightval:
            h.next = righthead
            return (h.val, h)
        else:
            return (rightval, righthead)