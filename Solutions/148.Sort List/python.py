# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def helper(self, head, length):
        if length == 0 or length == 1:
            return head
        # split the list
        first_len, second_len = length-length//2, length//2
        firsthead, secondhead = head, head
        for i in range(first_len):
            if i == first_len-1:
                temp = secondhead.next
                secondhead.next = None
                secondhead = temp
            else:
                secondhead = secondhead.next
        firsthead, secondhead = self.helper(firsthead, first_len), self.helper(secondhead, second_len)
        dummy = curr = ListNode(0)
        while firsthead != None and secondhead != None:
            if firsthead.val <= secondhead.val:
                curr.next = firsthead
                firsthead = firsthead.next
            else:
                curr.next = secondhead
                secondhead = secondhead.next
            curr = curr.next
        if firsthead != None:    curr.next = firsthead
        if secondhead != None:   curr.next = secondhead
        return dummy.next
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:    return head
        cnt, curr = 0, head
        while curr != None:
            curr = curr.next
            cnt += 1
        return self.helper(head, cnt)    