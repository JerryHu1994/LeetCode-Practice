# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
                return
            self.helper(root.right, val)
        else:
            if root.left == None:
                root.left = TreeNode(val)
                return
            self.helper(root.left, val)
    
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        self.helper(root, val)
        return root
        