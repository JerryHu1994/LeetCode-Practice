# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        curr = dummy_head
        if head.next == None:   return head
        if curr.next.val < 0:   curr = curr.next
        while curr.next != None:
            if curr.next.val < 0:
                # shift it to front
                nextnode = curr.next
                curr.next = nextnode.next
                nextnode.next = dummy_head.next
                dummy_head.next = nextnode
            else:
                curr = curr.next
        return dummy_head.next