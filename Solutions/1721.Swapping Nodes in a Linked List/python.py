# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:    return head
        curr, cnt = head, 0
        while curr != None:
            curr = curr.next
            cnt += 1
        left_ptr, right_ptr = head, head
        for i in range(k-1):    left_ptr = left_ptr.next
        for i in range(cnt-k):  right_ptr = right_ptr.next
        left_ptr.val, right_ptr.val = right_ptr.val, left_ptr.val
        return head
        