# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, head, length):
        if head==None:  return None
        if head.next == None:   return TreeNode(head.val)
        mid = int(length//2)
        curr = head
        for i in range(mid-1):
            curr = curr.next
        root = TreeNode(curr.next.val)
        righthead = curr.next.next
        curr.next = None
        left = self.helper(head, mid)
        right = self.helper(righthead, length - 1 - mid)
        root.left, root.right = left, right
        return root
        
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        totalLen = 0
        curr = head
        while curr != None:
            totalLen += 1
            curr = curr.next
        ret = self.helper(head, totalLen)
        return ret
        