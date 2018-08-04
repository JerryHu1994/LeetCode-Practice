# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:  return head
        dummy = ListNode(0)
        dummy.next = head
        pre = curr = dummy
        while True:
            currcount = 0
            nextpre = pre.next
            # move k steps further
            while curr != None:
                curr = curr.next
                currcount += 1
                if currcount == k:
                    break
            if currcount != k or curr == None:  break
            last = curr.next
            # reverse the nodes
            c = pre.next
            cc = c.next
            c.next = last
            while c != curr:
                temp = cc.next
                cc.next = c
                c, cc = cc, temp
            pre.next = curr
            #reset
            pre = curr = nextpre
        return dummy.next