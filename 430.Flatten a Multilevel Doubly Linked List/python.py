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
    
    # return the tail of the current level
    def helper(self, head):
        curr = head
        rettail = None
        while curr!=None:
            if curr.child != None:
                childhead = curr.child
                childtail = self.helper(childhead)
                currnext = curr.next
                if currnext != None:
                    curr.next, childhead.prev, childtail.next, currnext.prev = childhead, curr, currnext, childtail
                else:
                    curr.next, childhead.prev, childtail.next = childhead, curr, currnext
                curr = childtail
                if curr.next == None:   rettail = curr
            else:
                if curr.next == None:   rettail = curr
                curr = curr.next
        return rettail
        
        
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:    return head
        self.helper(head)
        curr = head
        while curr.next!=None:
            curr.child, curr = None, curr.next
        return head
        