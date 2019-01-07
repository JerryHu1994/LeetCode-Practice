# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or root.left == None:   return root
        left, right = root.left, root.right
        ret = self.upsideDownBinaryTree(left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return ret