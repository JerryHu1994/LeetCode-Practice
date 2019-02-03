# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, node):
        if node==None:  return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return 1+max(left,right)
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:   return True
        l = self.helper(root.left)
        r = self.helper(root.right)
        return abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)