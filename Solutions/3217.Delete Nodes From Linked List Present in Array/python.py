# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(0, None)
        dummy.next = head
        curr = dummy
        while curr.next != None:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next