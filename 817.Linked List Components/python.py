# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s = set(G)
        curr, ret, ingroup = head, 0, False
        while curr != None:
            if curr.val in s:
                ingroup = True
            else:
                if ingroup: ret += 1
                ingroup = False
            curr = curr.next
        if ingroup: ret += 1
        return ret