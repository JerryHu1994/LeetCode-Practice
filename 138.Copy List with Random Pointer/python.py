# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:    return head
        dic, curr = {}, head
        while curr != None:
            new = RandomListNode(curr.label)
            dic[curr] = new
            curr = curr.next
        old, new = head, dic[head]
        while old != None:
            new.next = dic[old.next] if old.next != None else None
            new.random = dic[old.random] if old.random != None else None
            new, old = new.next, old.next
        return dic[head]
            