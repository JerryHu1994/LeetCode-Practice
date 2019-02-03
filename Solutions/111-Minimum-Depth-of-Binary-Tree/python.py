# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:    return 0
        if root.left == None and root.right == None:
            return 1
        leftd = self.minDepth(root.left) if root.left != None else float("inf")
        rightd = self.minDepth(root.right) if root.right != None else float("inf")
        return min(leftd, rightd) + 1