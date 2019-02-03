# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        #count and split
        curr, count = root, 0
        while curr != None:
            count += 1
            curr = curr.next
        each, remain = count/k, count%k
        li = [each]*k
        for i in range(remain):
            li[i] += 1
        # split
        ret = []
        head = root
        for currnum in li:
            if head == None:
                ret.append(None)
                continue
            curr = head
            for i in range(currnum-1):
                curr = curr.next
            nexthead = curr.next
            curr.next = None
            ret.append(head)
            head = nexthead
        return ret
            