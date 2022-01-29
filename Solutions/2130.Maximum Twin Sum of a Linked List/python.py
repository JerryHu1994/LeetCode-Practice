# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n, curr = 0, head
        while curr != None:
            n += 1
            curr = curr.next
        curr, half = head, n//2
        for i in range(half-1):
            curr = curr.next
        secondhead = curr.next
        curr.next = None
        # reverse second half
        def reverse(node):
            if node.next == None:
                return node, node
            nodehead, topnode = reverse(node.next)
            nodehead.next = node
            return node, topnode
        lastnode, topnode = reverse(secondhead)
        lastnode.next = None
        res = 0
        firstptr, secondptr = head, topnode
        for i in range(half):
            res = max(res, firstptr.val+secondptr.val)
            firstptr = firstptr.next
            secondptr = secondptr.next
        return res
            