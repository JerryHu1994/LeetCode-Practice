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
        if root == None:    return
        curr = root
        nextleft = None
        while curr.left!=None:
            nextleft = curr.left if curr.left!=None else None
            while curr != None:
                curr.left.next = curr.right
                curr.right.next = None if curr.next == None else curr.next.left
                curr = curr.next
            curr = nextleft
                
            
    