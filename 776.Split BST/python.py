# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root == None:
            return [None, None]
        if V < root.val:
            ret = self.splitBST(root.left, V)
            root.left = ret[1]
            return [ret[0], root]
        else:
            ret = self.splitBST(root.right, V)
            root.right = ret[0]
            return [root, ret[1]]