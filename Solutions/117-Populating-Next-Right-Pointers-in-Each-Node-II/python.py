# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(0)
        pre, curr = dummy, root
        while curr != None:
            if curr.left!=None:
                pre.next = curr.left
                pre = pre.next
            if curr.right!=None:
                pre.next = curr.right
                pre = pre.next
            curr = curr.next
            if curr==None:
                pre = dummy
                curr = dummy.next
                dummy.next = None