# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:    return
        dummy = ListNode(0)
        dummy.next = head
        sortedhead = dummy
        sortedend = dummy.next
        while sortedend.next != None:
            currnode = sortedend.next
            currval = currnode.val
            if currval >= sortedend.val:
                sortedend = currnode
                continue
            insert = sortedhead
            sortedend.next = sortedend.next.next
            while insert != sortedend:
                if insert.next.val > currval :
                    insert.next, currnode.next = currnode, insert.next
                    break
                insert = insert.next
        return dummy.next
            
            