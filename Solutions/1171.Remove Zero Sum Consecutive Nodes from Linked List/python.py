# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        dummy = ListNode(0, head)
        currsum = 0
        curr = dummy.next
        dic[0] = dummy
        while curr != None:
            currsum += curr.val
            if currsum in dic:
                # move nodes from dic[currsum] to curr
                remove_curr = dic[currsum]
                remove_currsum = currsum
                while remove_curr != curr:
                    remove_curr = remove_curr.next
                    if remove_curr == curr: break   
                    remove_currsum += remove_curr.val
                    del dic[remove_currsum]
                dic[currsum].next = curr.next
            else:
                dic[currsum] = curr
            curr = curr.next
        return dummy.next