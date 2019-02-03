# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, minval, maxval):
        if root==None:  return True
        if ((maxval!=None and root.val>=maxval) or (minval!=None and root.val<=minval)):  return False
        return self.helper(root.left, minval, root.val) and self.helper(root.right, root.val, maxval)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, None, None)
        