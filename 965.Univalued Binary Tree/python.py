# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:    return True
        def helper(r, val):
            if r == None:   return True
            if r.val != val:
                return False
            else:
                return helper(r.left, val) and helper(r.right, val)
        return helper(root, root.val)