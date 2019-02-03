"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    
    # returns first node and last node, cannot be None
    def helper(self, root):
        if root.left != None:
            leftfirst, leftlast = self.helper(root.left)
            leftlast.right = root
            root.left = leftlast
        if root.right != None:
            rightfirst, rightlast = self.helper(root.right)
            root.right = rightfirst
            rightfirst.left = root
        retfirst = leftfirst if root.left != None else root
        retlast = rightlast if root.right != None else root
        return retfirst, retlast
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:  return root
        first, last = self.helper(root)
        first.left = last
        last.right = first
        return first