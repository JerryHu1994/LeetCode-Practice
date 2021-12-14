# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head == None or head.next == None:   return [-1, -1]
        curr_ptr = head.next
        pre_ptr = head
        curr_idx = 1
        first_critical = None
        pre_critical = None
        mindis, maxdis = float('inf'), 0
        while curr_ptr.next != None:
            if (pre_ptr.val < curr_ptr.val and curr_ptr.next.val < curr_ptr.val) or (pre_ptr.val > curr_ptr.val and curr_ptr.next.val > curr_ptr.val):
                if first_critical == None:
                    first_critical = curr_idx
                maxdis = curr_idx - first_critical
                if pre_critical != None:
                    mindis = min(mindis, curr_idx - pre_critical)
                pre_critical = curr_idx
                print (curr_idx)
            curr_idx += 1
            pre_ptr = curr_ptr
            curr_ptr = curr_ptr.next
            
        if mindis == float('inf') or maxdis == 0:
            return [-1, -1]
        return [mindis, maxdis]