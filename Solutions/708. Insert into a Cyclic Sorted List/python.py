"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head == None:
            return Node(insertVal, None)
        curr, currval, maxNode, firstrun = head, head.val, head, True
        while True:
            if firstrun:
                firstrun = False
            elif curr == head:
                break
            if curr.val <= insertVal and curr.next.val >= insertVal:
                # insert the value between curr and curr.next
                newnode = Node(insertVal, curr.next)
                curr.next = newnode
                return head
            if curr.val >= currval:
                maxNode = curr
                currval = curr.val
            curr = curr.next
        newnode = Node(insertVal, maxNode.next)
        maxNode.next = newnode
        return head
            