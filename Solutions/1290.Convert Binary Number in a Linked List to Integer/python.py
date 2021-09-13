# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        li = []
        curr = head
        while curr != None:
            li.append(curr.val)
            curr = curr.next
        ans = 0
        for ind, val in enumerate(li[::-1]):
            if val == 1:
                ans += math.pow(2, ind)
        return int(ans)