# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        pq = PriorityQueue()
        for i, n in enumerate(lists):
            if n!=None: pq.put((n.val, n))
        while not pq.empty():
            currmin = pq.get()
            currnode = currmin[1]
            if currnode.next != None:
                nextnode = currnode.next
                pq.put((nextnode.val, nextnode))
            curr.next = currnode
            curr = curr.next
        return dummy.next if len(lists) != 0 else None
