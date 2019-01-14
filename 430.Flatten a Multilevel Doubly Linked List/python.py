"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def helper(h):
            curr = h
            pre = h
            while curr != None:
                if curr.child:
                    nexthead, nexttail = helper(curr.child)
                    currnext = curr.next
                    curr.next, nexthead.prev, nexttail.next = nexthead, curr, currnext
                    if currnext != None:
                        currnext.prev = nexttail
                    curr.child = None
                    pre = nexttail
                    curr = currnext
                else:
                    pre = curr
                    curr = curr.next
            return h, pre
        return helper(head)[0]