# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummyHead = ListNode(0, list1)
        curr = dummyHead
        firstptr, secondptr = None, None
        for i in range(a):
            curr = curr.next
        firstptr = curr
        for i in range(b-a+2):
            curr = curr.next
        secondptr = curr
        curr2 = list2
        while curr2.next != None:
            curr2 = curr2.next
        firstptr.next = list2
        curr2.next = secondptr
        return dummyHead.next